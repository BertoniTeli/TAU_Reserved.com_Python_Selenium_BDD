Feature: Test login functionality

  Scenario: Login successfully
    Given open the authentication page
    When the user types username "testDaniel@yahoo.com"
    And the user types password "123456"
    And the user clicks the signin button
    Then the user is redirected to main page
    And the user is logged in as test

  Scenario Outline: Login unsuccessfully
    Given open the authentication page
    When the user types username "<username>"
    And the user types password "<password>"
    And the user clicks the signin button
    Then the user stayed on the authentication page
    And the error "<error>" message of "<error_type>" is displayed

    Examples: usernames, passwords and errors
      | username             | password | error                                          | error_type     |
      | testDaniel@yahoo.com | 12r43td  | Logare sau parolă nevalidă.                    | general_error  |
      | testDaniel@yahoo.com | 1234     | Logare sau parolă nevalidă.                    | general_error  |
      | testDaniel@yahoo.com | /        | Acest câmp este obligatoriu                    | password_error |
      | bestDaniel@yahoo.com | 123456   | Logare sau parolă nevalidă.                    | general_error  |
      | testDaniel           | 123456   | Vă rugăm să introduceți numai caractere valide | username_error |
      | /                    | 123456   | Acest câmp este obligatoriu                    | username_error |
    # Figured out that "/" is fed as blank space to the site
