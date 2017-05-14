# -*- coding: utf-8 -*-

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
def login(context):
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
def click_login(context):
    time.sleep(2)
    try:
        button = context.browser.find_element_by_css_selector(context.customapp.get_app_login_app_button())
        button.click()
        time.sleep(2)
    except (InvalidSelectorException, NoSuchElementException, InvalidElementStateException, InvalidSelectorException):
        assert 'STEP: click_login - Error trying to push login button'


@then(u'the user is succesfully logged in')
def successfull_login(context):
    login_user_field = True
    time.sleep(5)
    try:
        user_field = context.browser.find_element_by_css_selector(context.customapp.get_app_login_user_field())
    except (InvalidSelectorException, NoSuchElementException, InvalidElementStateException, InvalidSelectorException):
        login_user_field = False
    assert_that(login_user_field, is_(False),
                "STEP: successfull_login: Field login_user found, so the user can't log in")
