CKER TEST LOGIN

This pipeline contructs a docker that permits test a web login with user/pass credentials.

This docker will require the following parameters

|Field|Description|
|:----|----------:|
|BEHAVE_URL_LOGIN|URL witch you put user password|
|BEHAVE_USER_LOGIN|Login user|
|BEHAVE_USER_PASSWORD|Login password|
|BEHAVE_APP_LOGIN_USER|CSS locator for login field|
|BEHAVE_APP_LOGIN_PASS|CSS locator for password field|
|BEHAVE_APP_LOGIN_BUTTON|CSS locator for submit login form|

Creation
```
docker build -t test_login .
```

Execution
```
docker run --env-file variables test_login
```

# Exit examples

**Good test**
```
Feature: Operator login # authorization.feature:3
  As an application owner
  I want to be able to log into the system
  In order to operate with the tool
  @login @browser
  Scenario: Successful login                                         # authorization.feature:9
    Given a browser and is opened to login page                      # steps/step_authorization.py:22
    When the user enters name "GOODUSER" and password "GOODPASSWORD" # steps/step_authorization.py:45
    And the user click on login button                               # steps/step_authorization.py:72
    Then the user is succesfully logged in                           # steps/step_authorization.py:84

1 feature passed, 0 failed, 0 skipped
1 scenario passed, 0 failed, 0 skipped
4 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m16.338s
```

**Bad test**
```
Feature: Operator login # authorization.feature:3
  As an application owner
  I want to be able to log into the system
  In order to operate with the tool
  @login @browser
  Scenario: Successful login                                         # authorization.feature:9
    Given a browser and is opened to login page                      # steps/step_authorization.py:22
    When the user enters name "GOODUSER" and password "GOODPASSWORD" # steps/step_authorization.py:45
    And the user click on login button                               # steps/step_authorization.py:72
    Then the user is succesfully logged in                           # steps/step_authorization.py:84
      Assertion Failed: STEP: successfull_login: Field login_user found, so the user can't log in
      Expected: <False>
           but: was <True>



Failing scenarios:
  authorization.feature:9  Successful login

0 features passed, 1 failed, 0 skipped
0 scenarios passed, 1 failed, 0 skipped
3 steps passed, 1 failed, 0 skipped, 0 undefined
Took 0m11.007s
```
