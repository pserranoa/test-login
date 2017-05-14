# -*- coding: UTF-8 -*-

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
from application_objects import WebAppData


def before_all(context):
    # driver de visualizacion para entornos no X
    context.config.setup_logging()
    context.customapp = WebAppData("AppTest")
    usage = """
            BEHAVE_URL_LOGIN - URL where you put user password
            BEHAVE_USER_LOGIN - login user
            BEHAVE_USER_PASSWORD - login password
            BEHAVE_APP_LOGIN_USER - css locator for login field
            BEHAVE_APP_LOGIN_PASS - css locator for password field
            BEHAVE_APP_LOGIN_BUTTON - css locator for submit login form
            """

    try:
        env_url_login = os.environ['BEHAVE_URL_LOGIN']
    except KeyError:
        print("BEHAVE_URL_LOGIN not found\n")
        raise SystemExit(usage)
    context.customapp.set_urllogin(env_url_login)

    try:
        env_default_user_login = os.environ['BEHAVE_USER_LOGIN']
    except KeyError:
        print ("BEHAVE_USER_LOGIN not found\n")
        raise SystemExit(usage)
    context.customapp.set_userlogin(env_default_user_login)

    try:
        env_default_user_password = os.environ['BEHAVE_USER_PASSWORD']
    except KeyError:
        print("BEHAVE_USER_PASSWORD not found\n")
        raise SystemExit(usage)
    context.customapp.set_passlogin(env_default_user_password)

    try:
        env_app_login_user = os.environ['BEHAVE_APP_LOGIN_USER']
    except KeyError:
        print("BEHAVE_APP_LOGIN_USER not found\n")
        raise SystemExit(usage)
    context.customapp.set_app_login_user_field(env_app_login_user.replace('"', ""))

    try:
        env_app_login_pass = os.environ['BEHAVE_APP_LOGIN_PASSWORD']
    except KeyError:
        print("BEHAVE_APP_LOGIN_PASSWORD not found\n")
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
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--no-sandbox')
        context.browser = webdriver.Chrome(chrome_options=options)

def after_scenario(context, scenario):
        context.browser.close()

def alter_all(context):
    context.display.stop()
