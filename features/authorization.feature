# lenguage: en
@browser
Feature: Web login
	As an application owner
	I want to be able to log into the system

@login @browser
    Scenario: Successful login
        Given a browser and is opened to login page
        When the user enters name "GOODUSER" and password "GOODPASSWORD"
		    And the user click on login button
        Then the user is succesfully logged in
