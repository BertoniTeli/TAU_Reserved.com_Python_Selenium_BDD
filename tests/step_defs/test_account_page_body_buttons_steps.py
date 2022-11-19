from pytest_bdd import scenarios, given, when, parsers, then
from selenium.webdriver.common.by import By

from pages.account_page import AccountPageBody
from pages.authentication_page import LoginPage
from utils.usefull_elements import SignIn

scenarios('../features/test_account_page_body_buttons.feature')


@given('open the account page')
def load_page(browser):
    LoginPage(browser).load_page()
    LoginPage(browser).set_user_inputs()
    AccountPageBody(browser).enter_account_menu()
    print("\n---Step 1---Given---Pass---")


@given('the user is logged in as test')
def check_user_is_logged_in(browser):
    account_name = browser.find_element(By.CSS_SELECTOR, "[data-testid='account-info-logged-true']").text
    # The Reserved site has a bug that alters the letters to uppercase
    account_name = str.lower(account_name)
    assert account_name == SignIn.TEST_FIRSTNAME
    print("\n---Step 2---Given---Pass---")


@when(parsers.cfparse('the user clicks "{button}" named "{name}"'))
def check_button_name_and_click_it(browser, button, name):
    button_name = browser.find_element(By.LINK_TEXT, f"{button}").get_attribute("innerHTML")
    assert button_name == name
    AccountPageBody(browser).click_account_menu_buttons(button)
    print("\n---Step 3---When---Pass---")


@then(parsers.cfparse('the user is redirected to "{page}"'))
def check_user_redirected_to_page(browser, page):
    assert browser.current_url == page, "Main page URL is not ok."
    print("\n---Step 4---Then---Pass---")


@then('the user is logged in as test')
def check_user_is_logged_in(browser):
    if browser.current_url == "https://www.reserved.com/ro/ro/":
        return "pass"
    account_name = browser.find_element(By.CSS_SELECTOR, '[data-testid="account-info-logged-true"]').text
    account_name = str.lower(account_name)
    assert account_name == SignIn.TEST_FIRSTNAME
    print("\n---Step 5---Then---Pass---")


@then(parsers.cfparse('the "{button}" is named "{name}"'))
def check_button_name(browser, button, name):
    if browser.current_url == "https://www.reserved.com/ro/ro/":
        return "pass"
    button_name = AccountPageBody(browser).get_account_menu_buttons_name(button)
    if name == "Adresă de facturare":
        name = "Adresa de facturare"
    elif name == "Setările contului":
        name = "Setarile contului"
    assert button_name == name
    print("\n---Step 6---Then---Pass---")
