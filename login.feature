Feature: Login

  Scenario: Login to OrangeHRM
        Given  we are at "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        When   enter username and password
        And    click on login button
        Then   are successfully logged in


