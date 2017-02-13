# -*- coding: utf-8 -*-

""""
Module: behave
File: step_authorization.py
Description: steps
Authors: Pedro Serrano
"""

import time

from behave import *
from selenium import webdriver
from selenium.common.exceptions import *
from hamcrest import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui

@given(u'a browser and is opened to login page')
@given(u'the login page is loaded')
def login(context):
    # verify that the user field appears
    login_user_field = True
    context.browser.get(context.customapp.get_urllogin())
    try:
        ui.WebDriverWait(context.browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,
        context.customapp.get_app_login_user_field())))
        login_user_field = True
    except TimeoutException:
        login_user_field = False
    if login_user_field:
        try:
            user_field = context.browser.find_element_by_css_selector(
            context.customapp.get_app_login_user_field())
        except (InvalidSelectorException, NoSuchElementException,
                InvalidElementStateException, InvalidSelectorException):
            login_user_field = False
    assert_that(login_user_field, is_(True), "STEP: login - Open Login Page: Field login_user not found")


@when(u'the user enters name "{user}" and password "{passwd}"')
def authenticate(context, user, passwd):
    username_field = True;
    password_field = True
    try:
        username = context.browser.find_element_by_css_selector(context.customapp.get_app_login_user_field())
        username.clear()
    except (InvalidSelectorException, NoSuchElementException, InvalidElementStateException, InvalidSelectorException):
        username = False

    if user.upper() == "GOODUSER":
        username.send_keys(context.customapp.get_userlogin())
    else:
        username.send_keys(user)
    try:
        password = context.browser.find_element_by_css_selector(context.customapp.get_app_login_pass_field())
        password.clear()
    except (InvalidSelectorException, NoSuchElementException, InvalidElementStateException, InvalidSelectorException):
        password = False
    if passwd.upper() == "GOODPASSWORD":
        password.send_keys(context.customapp.get_passlogin())
    else:
        password.send_keys(passwd)
    assert_that(username_field, is_(True), "STEP: authenticate - Field login_user not found")
    assert_that(password_field, is_(True), "STEP: authenticate - Field login_pass not found")


@when(u'the user click on login button')
@given(u'the user click on login button')
def click_login(context):
    time.sleep(2)
    try:
        button = context.browser.find_element_by_css_selector(context.customapp.get_app_login_app_button())
        button.click()
        time.sleep(2)
    except (InvalidSelectorException, NoSuchElementException, InvalidElementStateException, InvalidSelectorException):
        assert 'STEP: click_login - Error trying to push login button'


@then(u'the user is succesfully logged in')
@when(u'the user logs in correctly')
def successfull_login(context):
    # if the browser is directed to the home page
    # the page doest not show the login_field
    login_user_field = True
    #context.browser.get(context.customapp.get_urllogin())
    time.sleep(5)
    try:
        user_field = context.browser.find_element_by_css_selector(context.customapp.get_app_login_user_field())
    except (InvalidSelectorException, NoSuchElementException, InvalidElementStateException, InvalidSelectorException):
        login_user_field = False
    #if login_user_field == False:
    #    context.browser.save_screenshot('./reports/'+context.feature.filename.replace(r'features/', '')+'/'+context.scenario.name+'_login.png')
    assert_that(login_user_field, is_(False),
                "STEP: successfull_login: Field login_user found, so the user can't log in")
    # SAVE COOKIES AFTER LOGIN OK
    # get cookies names from default_cookies_defined
    app_cookies_name_list = [cookie[0] for cookie in context.customapp.get_def_cookies()]
    login_cookies = context.browser.get_cookies()
    list_app_cookies = []
    for cookie in login_cookies:
        if cookie['name'] in app_cookies_name_list:
            list_app_cookies.append(cookie)
    context.customapp.set_cookies(list_app_cookies)


@then(u'the user is not logged in')
@then(u'the user is not logged')
def unsuccessfull_login(context):
    context.browser.get(context.customapp.get_urllogin())
    login_user_field = True
    try:
        user_field = context.browser.find_element_by_css_selector(context.customapp.get_app_login_user_field())
    except (InvalidSelectorException, NoSuchElementException, InvalidElementStateException, InvalidSelectorException):
        login_user_field = False
    assert_that(login_user_field, is_(True),
                "STEP: unsuccessful_login: Field login_user found, so the user can log in")


@when(u'the user logout')
@when(u'the user logs out')
def successfull_logout(context):
    logoutbutton = True
    try:
        # step by step until click logout button
        for button in context.customapp.get_app_logout_app_button():
            logout_button = context.browser.find_element_by_css_selector(button)
            logout_button.click()
            time.sleep(5)
    except (InvalidSelectorException, NoSuchElementException, InvalidSelectorException,
            InvalidElementStateException, ElementNotVisibleException):
        logoutbutton = False
    assert_that(logoutbutton, is_(True),
                "STEP: successful_logout: button logout not found, so the user still loged in")
    time.sleep(5)
    cookies = context.browser.get_cookies()
    app_cookies_name_list = [cookie[0] for cookie in context.customapp.get_def_cookies()]
    for cookie in cookies:
        if cookie['name'] in app_cookies_name_list:
            assert_that(str(cookie['value']), has_length,
                        "STEP: successful_logout - cookie %s has value %s" % (cookie['name'], cookie['value']))
