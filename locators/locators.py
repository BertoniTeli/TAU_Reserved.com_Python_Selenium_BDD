from selenium.webdriver.common.by import By


class LogInLocators:
    URL = "https://www.reserved.com/ro/ro/customer/account/login/#login"
    accept_cookies_button = (By.CSS_SELECTOR, "#cookiebotDialogOkButton")
    login_email_box = (By.CSS_SELECTOR, "#login\[username\]_id")
    login_password_box = (By.CSS_SELECTOR, "#login\[password\]_id")
    login_button = (By.CSS_SELECTOR, ".primary__PrimaryButtonComponent-sc-1pct4vx-0")
    center_error_message = (By.CSS_SELECTOR, ".sc-dlfnuX")
    email_error_message = (By.XPATH, "/html//form/div[1]/div/div")
    password_error_message = (By.XPATH, "/html//form/div[2]/div/div")


class CreateAccountLocators:
    URL = "https://www.reserved.com/ro/ro/customer/account/login/#login"
    create_account_button = (By.CSS_SELECTOR, ".button__ButtonPrimary-zerqf2-0")
    create_account_email_box = (By.CSS_SELECTOR, "#email_id")
    create_account_password_box = (By.CSS_SELECTOR, "#password_id")
    create_account_firstname_box = (By.CSS_SELECTOR, "#firstname_id")
    create_account_lastname_box = (By.CSS_SELECTOR, "#lastname_id")
    create_account_confirm_button = (By.CSS_SELECTOR, '[data-selen="create-account-submit"]')


class AccountPageLocators:
    URL = "https://www.reserved.com/ro/ro/sales/order/history/"
    accept_cookies_button = (By.CSS_SELECTOR, "#cookiebotDialogOkButton")
    body_title = (By.CSS_SELECTOR, "[.orders-list__TitleText-fwoa0w-2]")
    account_menu = (By.CSS_SELECTOR, '[data-testid="account-info-logged-true"]')
    close_newsletter_popup_button = (By.CSS_SELECTOR, "div.close")

    # Comenzile mele -- buton
    order_history_button = (By.CSS_SELECTOR, '[data-testid="orderHistory"]')
    URL_order_history = "https://www.reserved.com/ro/ro/sales/order/history"

    # Retururile mele -- buton
    return_list_button = (By.CSS_SELECTOR, 'li [data-testid="returns"]')
    URL_return_list = "https://www.reserved.com/ro/ro/myaccount/return/list/"

    # Setările contului -- buton
    edit_account_button = (By.CSS_SELECTOR, 'li [data-testid="account"]')
    edit_account_button_bug = (By.CSS_SELECTOR, ".change-customer-data")

    # Adrese de livrare -- buton
    address_data_button = (By.CSS_SELECTOR, 'li [data-testid="addresses"]')
    address_data_button_bug = (By.CSS_SELECTOR, ".change-address")

    # Adresă de facturare -- buton
    invoice_data_button = (By.CSS_SELECTOR, 'li [data-testid="invoices"]')
    invoice_data_button_bug = (By.CSS_SELECTOR, ".change-invoice-address")

    # Delogare -- buton
    logout_button = (By.CSS_SELECTOR, 'li [data-testid="logout"]')


class MainPageLocators:
    URL = "https://www.reserved.com/ro/ro/"
    displayed_user_name = (By.CSS_SELECTOR, "[//div/div/text()[contains(., 'test')]]")
    logout_button = (By.CSS_SELECTOR, '[data-testid="logout"]')
