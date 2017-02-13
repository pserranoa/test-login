# lenguage: en
@browser
Feature: Operator login
	As an application owner
	I want to be able to log into the system
	In order to operate with the tool

@login @browser
    Scenario: Successful login
        Given a browser and is opened to login page
        When the user enters name "GOODUSER" and password "GOODPASSWORD"
		    And the user click on login button
        Then the user is succesfully logged in
