from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from locators.locators import MainPageLocators, LogInLocators
from pages.login_page import LoginPage
from utils.usefull_elements import SignIn

scenarios('../features/test_sign_in.feature')


@given('open the authentication page')
def load_page(browser):
    LoginPage(browser).load_page()


@when(parsers.cfparse('the user types username "{username}"'))
def type_username(browser, username):
    if username == '/':
        username = ""
    LoginPage(browser).type_email(username)


@when(parsers.cfparse('the user types password "{password}"'))
def type_password(browser, password):
    if password == "/":
        password = ""
    LoginPage(browser).type_password(password)


@when('the user clicks the signin button')
def click_sign_in(browser):
    LoginPage(browser).click_sign_in()


@then('the user is redirected to main page')
def check_user_redirected_to_main_page(browser):
    WebDriverWait(browser, 5).until(ec.url_changes(LogInLocators.URL))
    assert browser.current_url == MainPageLocators.URL, "Main page URL is not ok."


@then('the user stayed on the authentication page')
def check_user_stayed_on_authentication_page(browser):
    assert browser.current_url == LogInLocators.URL, "Authentication page URL is not ok."


@then('the user is logged in as test')
def check_user_name_displayed(browser):
    account_name = browser.find_element(By.CSS_SELECTOR, '[data-testid="account-info-logged-true"]').text
    account_name = str.lower(account_name)
    assert account_name == SignIn.TEST_FIRSTNAME


@then(parsers.cfparse('the error "{error_message}" message of "{error_type}" is displayed'))
def check_error_message(browser, error_message, error_type):
    assert LoginPage(browser).get_error_message(error_type) == error_message
