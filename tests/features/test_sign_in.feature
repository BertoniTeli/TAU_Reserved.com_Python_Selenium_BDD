Feature: Test login functionality

  Scenario: Login successfully
    Given open the authentication page
    When the user types username
    And the user types password
    And the user clicks the signin button
    Then the user is redirected to main page
    And the user is logged in as test
    And the logout button is displayed

  Scenario Outline: Login unsuccessfully
    Given open the authentication page
    When the user types username "<username>"
    And the user types password "<password>"
    And the user clicks the signin button
    Then the user stayed on the authentication page
    And the error "<error>" message is displayed

    Examples: usernames, passwords and errors
      | username             | password | error                                          |
      | testDaniel@yahoo.com | 12r43td  | Logare sau parolă nevalidă.                    |
      | testDaniel@yahoo.com | 1234     | Logare sau parolă nevalidă.                    |
      | testDaniel@yahoo.com | \        | Acest câmp este obligatoriu                    |
      | bestDaniel@yahoo.com | 123456   | Logare sau parolă nevalidă.                    |
      | testDaniel           | 123456   | Vă rugăm să introduceți numai caractere valide |
      | \                    | 123456   | Acest câmp este obligatoriu                    |
    # Figured out that "\" is fed as blank space to the site
