Feature: EPAM site
  Scenario: "Menu" button working
      Given we are at "https://www.epam.com/"
      When we push "Menu" button
      Then dropdown navigation bar displays

  Scenario: "linkedin" button working
    Given we are at "https://www.epam.com/"
    And we scrolled to the bottom of the page
    When we push the "linkedin" icon button
    Then we readdressed to "https://www.linkedin.com/company/epam-systems/"


Feature: Start Your EPAM Career Journey
  Scenario:  "Apply" button working
      Given we are at "https://www.epam.com/careers"
      When we push "Apply" button
      Then we readdressed to "https://www.epam.com/careers/apply-now"

  Scenario: Not all required fields are filled
      Given we didn't filled any required fields
      When we submit request
      Then we get "This is a required field" message on all not filled required fields

  Scenario: All required fields are filled correctly
      Given we filled all required fields
      And all fields are correct
      When we submit request
      Then request is sent

  Scenario: "Privacy Notice" checkbox is not checked
      Given we didn't checked "Privacy Notice" checkbox
      When we submit request
      Then the color of checkbox changes to red

  Scenario Outline: Email is not correct
      Given we filled email field with <incorrectEmail>
      When we submit request
      Then we see <warning> about email field

      Examples:
        | incorrectEmail | warning                 |
        | someText       | Incorrect email format. |
        | someText@text  |                         |
        | someText.com   |                         |

  Scenario Outline: Phone is not correct
      Given we filled Phone field with <incorrectEmail>
      When we submit request
      Then we see <warning> about Phone field

      Examples:
        | incorrectEmail | warning                                                                                  |
        | someText       | Only digits, space, plus, and semicolon are allowed. Maximum number of characters is 50. |
        | 95text         |                                                                                          |
    
