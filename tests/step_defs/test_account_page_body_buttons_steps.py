from pytest_bdd import scenarios, given, when, parsers, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from locators.locators import AccountPageLocators
from pages.account_page import AccountPageBody
from pages.authentication_page import LoginPage
from utils.usefull_elements import SignIn

scenarios('../features/test_account_page_body_buttons.feature')


@given('open the account page')
def load_page(browser):
    AccountPageBody(browser).load_page()
    LoginPage(browser).set_user_inputs()


@given('the user is logged in as test')
def check_user_is_logged_in(browser):
    account_name = browser.find_element(By.CSS_SELECTOR, "[data-testid='account-info-logged-true']").text
    # The Reserved site has a bug that alters the letters to uppercase
    account_name = str.lower(account_name)
    assert account_name == SignIn.TEST_FIRSTNAME
    print("\n---when---User is logged in as 'test'.")


@when(parsers.cfparse('the user clicks "{button}" named "{name}"'))
def click_button_and_check_name(browser, button, name):
    button_name = browser.find_element(By.LINK_TEXT, f"{button}").get_attribute("innerHTML")
    if name == "Adresă de facturare":
        name = "Adresa de facturare"
        print(name)
    elif name == "Setările contului":
        name = "Setarile contului"
        print(name)
    else:
        print(name)
    print(f"\nChecking {button}...")
    assert button_name == name
    AccountPageBody(browser).click_order_history_button()


@then(parsers.cfparse('the user is redirected to "{page}"'))
def check_user_redirected_to_page(browser, page):
    WebDriverWait(browser, 5).until(ec.url_changes(AccountPageLocators.URL_order_history))
    assert browser.current_url == page, "Main page URL is not ok."
    print("\n---then---User is redirected to the right page.")


@then('the user is logged in as test')
def check_user_is_logged_in(browser):
    account_name = browser.find_element(By.CSS_SELECTOR, "[data-testid='account-info-logged-true']").text
    # The Reserved site has a bug that alters the letters to uppercase
    account_name = str.lower(account_name)
    assert account_name == SignIn.TEST_FIRSTNAME
    print("\n---then---User is logged in as 'test'.")


@then(parsers.cfparse('the "{button}" is named "{name}"'))
def check_button_name(browser, button, name):
    button_name = browser.find_element(By.CSS_SELECTOR, '[data-testid="orderHistory"]').text
    if name == "Adresă de facturare":
        name = "Adresa de facturare"
        print(name)
    elif name == "Setările contului":
        name = "Setarile contului"
        print(name)
    else:
        print(name)
    print(f"\nChecking {button}...")
    assert button_name == name, f"\nButton {button}'s name is not the same!"
