# -*- coding: utf-8 -*-

class WebAppData(object):
    def __init__(self, name, urllogin="", userlogin="", passlogin="",
    browser="",app_login_user_field="", app_login_pass_field="",
    app_login_app_button=""):
        self.name = name
        self.urllogin = urllogin
        self.userlogin = userlogin
        self.passlogin = passlogin
        self.browser = browser
        self.app_login_user_field = app_login_user_field
        self.app_login_pass_field = app_login_pass_field
        self.app_login_app_button = app_login_app_button

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_urllogin(self, urllogin=""):
        self.urllogin = urllogin

    def get_urllogin(self):
        return self.urllogin

    def set_userlogin(self,userlogin=""):
        self.userlogin = userlogin

    def get_userlogin(self):
        return self.userlogin

    def set_passlogin(self,passlogin=""):
        self.passlogin = passlogin

    def get_passlogin(self):
        return self.passlogin

    def get_browser(self):
        return self.browser

    def set_browser(self,browser="Chrome"):
        self.browser = browser

    def get_app_login_user_field(self):
        return self.app_login_user_field

    def set_app_login_user_field(self,app_login_user_field=""):
        self.app_login_user_field = app_login_user_field

    def get_app_login_pass_field(self):
        return self.app_login_pass_field

    def set_app_login_pass_field(self,app_login_pass_field=""):
        self.app_login_pass_field = app_login_pass_field

    def get_app_login_app_button(self):
        return self.app_login_app_button

    def set_app_login_app_button(self,app_login_app_button=""):
        self.app_login_app_button = app_login_app_button
