
from pytest_bdd import scenarios, given, when, then, parsers
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from locators.locators import MainPageLocators, LogInLocators
from pages.authentication_page import LoginPage
from utils.usefull_elements import SignIn

scenarios('../features/test_sign_in.feature')


@given('open the authentication page')
def load_page(browser):
    LoginPage(browser).load_page()


@when('the user types username')
def type_username(browser):
    LoginPage(browser).box_email_sign_in()


@when(parsers.cfparse('the user types username "{username}"'))
def type_username(browser, username):
    LoginPage(browser).box_email_sign_in_unsuccessfully(username)


@when('the user types password')
def type_password(browser):
    LoginPage(browser).box_password_sign_in()


@when(parsers.cfparse('the user types password "{password}"'))
def type_password(browser, password):
    LoginPage(browser).box_password_sign_in_unsuccessfully(password)


@when('the user clicks the signin button')
def click_sign_in(browser):
    LoginPage(browser).click_sign_in()


@then('the user is redirected to main page')
def check_user_redirected_to_main_page(browser):
    WebDriverWait(browser, 5).until(ec.url_changes(LogInLocators.URL))
    assert browser.current_url == MainPageLocators.URL, "Main page URL is not ok."
    print("\n---then---User is redirected to main page.")


@then('the user stayed on the authentication page')
def check_user_stayed_on_authentication_page(browser):
    WebDriverWait(browser, 2)
    assert browser.current_url == LogInLocators.URL, "Authentication page URL is not ok."
    print("\n---then---User stayed on the authentication page.")


@then(parsers.cfparse('the error "{error}" message is displayed'))
def check_error_message_displayed(browser, error):
    global error_list, current_error
    print(error)

    try:
        center_error = browser.find_element(By.CSS_SELECTOR, ".sc-dlfnuX")
    except NoSuchElementException:
        print("No centrall error occurred.")
    else:
        error_list = [center_error]
        current_error = browser.find_element(By.CSS_SELECTOR, ".sc-dlfnuX").get_attribute("innerHTML")
        print(current_error)
        return current_error

    try:
        email_error = browser.find_element(By.XPATH, "/html//form/div[1]/div/div")
    except NoSuchElementException:
        print("No email error occurred.")
    else:
        error_list = [email_error]
        current_error = browser.find_element(By.XPATH, "/html//form/div[2]/div/div").get_attribute("innerHTML")
        return current_error

    try:
        password_error = browser.find_element(By.XPATH, "/html//form/div[2]/div/div")
    except NoSuchElementException:
        print("No password error occurred.")
    else:
        error_list = [password_error]
        current_error = browser.find_element(By.XPATH, "/html//form/div[2]/div/div").get_attribute("innerHTML")
        print(current_error)
        return current_error

    print(current_error)
    assert current_error == error


@then('the user is logged in as test')
def check_user_name_displayed(browser):
    account = browser.find_element(By.CSS_SELECTOR, "[data-testid='account-info-logged-true']").text
    # The Reserved site has a bug that alters the letters to uppercase
    account = str.lower(account)
    assert account == SignIn.TEST_FIRSTNAME
    print("\n---then---User is logged in as 'test'.")


@then('the logout button is displayed')
def check_logout_button_displayed(browser):
    assert browser.find_element(By.CSS_SELECTOR, '[data-testid="logout"]')
    print("\n---then---Logout button is displayed.")
