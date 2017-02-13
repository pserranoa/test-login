# -*- coding: utf-8 -*-

class WebAppData(object):
    def __init__(self, name, urllogin="", userlogin="", passlogin="", cookies={}, urllogout="",fqdn="",
                 browser="",visualizacion=False,potocol="",port="",def_cookies=[],
                 app_login_user_field="", app_login_pass_field="",app_login_app_button="",
                 app_logout_app_button=[]):
        self.name = name
        self.urllogin = urllogin
        self.userlogin = userlogin
        self.passlogin = passlogin
        self.cookies = cookies
        self.urllogout = urllogout
        self.urlhome = ""
        self.fqdn = fqdn
        self.browser = browser
        self.visualizacion = visualizacion
        self.protocol = ""
        self.port = port
        self.def_cookies = []
        self.app_login_user_field = app_login_user_field
        self.app_login_pass_field = app_login_pass_field
        self.app_login_app_button = app_login_app_button
        self.app_logout_app_button = []

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

    def set_cookies(self,cookies=[]):
        self.cookies = cookies

    def get_cookies(self):
        return self.cookies

    def get_urllogout(self):
        return self.urllogout

    def set_urllogout(self,urllogout=""):
        self.urllogout = urllogout

    def get_urlhome(self):
        return self.urlhome

    def set_urlhome(self,urlhome=""):
        self.urlhome = urlhome

    def get_fqdn(self):
        return self.fqdn

    def set_fqdn(self,fqdn=""):
        self.fqdn = fqdn

    def get_browser(self):
        return self.browser

    def set_browser(self,browser="Firefox"):
        self.browser = browser

    def get_visualization(self):
        return self.visualizacion

    def set_visualization(self,visualizacion=False):
        self.visualizacion = visualizacion

    def get_protocol(self):
        return self.protocol

    def set_protocol(self,protocol="https"):
        self.protocol = protocol

    def get_port(self):
        return self.port

    def set_port(self,port="443"):
        self.port = port

    def get_def_cookies(self):
        return self.def_cookies

    def set_def_cookies(self,def_cookies=[]):
        self.def_cookies = def_cookies

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

    def get_app_logout_app_button(self):
        return self.app_logout_app_button

    def set_app_logout_app_button(self,app_logout_app_button=[]):
        self.app_logout_app_button = app_logout_app_button
