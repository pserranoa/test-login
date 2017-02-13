# -*- coding: UTF-8 -*-

""""
Module: behave
File: environment.py
Description: PRE and POST events of scenarios and steps
Authors: Pedro Serrano
"""

import signal
import os.path
import os

# -- SETUP: Use cfparse as default matcher
# from behave import use_step_matcher
# step_matcher("cfparse")
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.color import Color
from selenium.webdriver.remote.command import Command
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException

#
# custom import
#
# from .application_objects import *
from application_objects import WebAppData

__doc__ = """
before_step(context, step), after_step(context, step)
    These run before and after every step.
    The step passed in is an instance of Step.

before_scenario(context, scenario), after_scenario(context, scenario)
    These run before and after each scenario is run.
    The scenario passed in is an instance of Scenario.

before_feature(context, feature), after_feature(context, feature)
    These run before and after each feature file is exercised.
    The feature passed in is an instance of Feature.

before_tag(context, tag), after_tag(context, tag)

"""


def before_all(context):
    # driver de visualizacion para entornos no X
    context.config.setup_logging()
    context.customapp = WebAppData("AppTest")
    usage = """
    BEHAVE_HOST_FQDN - ip or fqnd name to test
    BEHAVE_HOST_PORT - port where listen front (80/443)
    BEHAVE_HOST_PROTOCOL - protocol configured (http/https)
    BEHAVE_DEFAULT_USER_LOGIN - login user
    BEHAVE_DEFAULT_USER_PASSWORD - login password
    BEHAVE_APP_LOGIN_USER - css locator for login field
    BEHAVE_APP_LOGIN_PASS - css locator for password field
    BEHAVE_APP_LOGIN_BUTTON - css locator for submit login form
    """

    try:
        env_host_fqdn = os.environ['BEHAVE_HOST_FQDN']
    except KeyError:
        print ("BEHAVE_HOST_FQDN not found")
        raise SystemExit(usage)
    context.customapp.set_fqdn(env_host_fqdn)

    try:
        env_host_port = os.environ['BEHAVE_HOST_PORT']
    except KeyError:
        print ("BEHAVE_HOST_PORT not found\n")
        raise SystemExit(usage)
    context.customapp.set_port(env_host_port)

    try:
        env_host_protocol = os.environ['BEHAVE_HOST_PROTOCOL']
    except KeyError:
        print("BEHAVE_HOST_PROTOCOL not found\n")
        raise SystemExit(usage)
    context.customapp.set_protocol(env_host_protocol)

    url_port = context.customapp.get_port()
    protocol = context.customapp.get_protocol()
    context.customapp.set_urlhome(
        protocol + "://" + context.customapp.get_fqdn() + ":" + url_port)
    context.customapp.set_urllogin(
        protocol + "://" + context.customapp.get_fqdn() + ":" + url_port)
    try:
        env_default_user_login = os.environ['BEHAVE_DEFAULT_USER_LOGIN']
    except KeyError:
        print ("BEHAVE_DEFAULT_USER_LOGIN not found\n")
        raise SystemExit(usage)
    context.customapp.set_userlogin(env_default_user_login)

    try:
        env_default_user_password = os.environ['BEHAVE_DEFAULT_USER_PASSWORD']
    except KeyError:
        print("BEHAVE_DEFAULT_USER_PASSWORD not found\n")
        raise SystemExit(usage)
    context.customapp.set_passlogin(env_default_user_password)

    try:
        env_app_login_user = os.environ['BEHAVE_APP_LOGIN_USER']
    except KeyError:
        print("BEHAVE_APP_LOGIN_USER not found\n")
        raise SystemExit(usage)
    context.customapp.set_app_login_user_field(env_app_login_user.replace('"', ""))

    try:
        env_app_login_pass = os.environ['BEHAVE_APP_LOGIN_PASS']
    except KeyError:
        print("BEHAVE_APP_LOGIN_PASS not found\n")
        raise SystemExit(usage)
    context.customapp.set_app_login_pass_field(env_app_login_pass.replace('"', ""))

    try:
        env_app_login_button = os.environ['BEHAVE_APP_LOGIN_BUTTON']
    except KeyError:
        print("BEHAVE_APP_LOGIN_BUTTON not found\n")
        raise SystemExit(usage)
    context.customapp.set_app_login_app_button(env_app_login_button.replace('"', ""))

    context.display = Display(visible=0, size=(800, 600))
    context.display.start()

def before_scenario(context, scenario):
        profile = webdriver.FirefoxProfile()
        profile.accept_untrusted_certs = True
        context.browser = webdriver.Firefox(firefox_profile=profile)
        context.browser.implicitly_wait(5)

def after_scenario(context, scenario):
        context.browser.close()
        context.browser.quit()

def alter_all(context):
    if context.customapp.get_visualization() == "False":
        context.display.stop()
