Feature: Test Account page body buttons

  Scenario Outline: Verify body buttons
    Given open the account page
    And the user is logged in as test
    When the user clicks "<button>" named "<name>"
    Then the user is redirected to "<page>"
    And the user is logged in as test
    And the "<button>" is named "<name>"

    Examples: button, name, page
      | button              | name                | page                                                               |
      | Comenzile mele      | Comenzile mele      | https://www.reserved.com/ro/ro/sales/order/history                 |
      | Retururile mele     | Retururile mele     | https://www.reserved.com/ro/ro/myaccount/return/list/              |
      | Setările contului   | Setările contului   | https://www.reserved.com/ro/ro/customer/account/edit/              |
      | Adrese de livrare   | Adrese de livrare   | https://www.reserved.com/ro/ro/customer/account/edit/#address-data |
      | Adresă de facturare | Adresa de facturare | https://www.reserved.com/ro/ro/customer/account/edit/#address-data |
      | Delogare            | Delogare            | https://www.reserved.com/ro/ro/                                    |