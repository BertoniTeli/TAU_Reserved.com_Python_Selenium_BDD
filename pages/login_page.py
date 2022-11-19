from time import sleep
from selenium.webdriver.common.by import By

from locators.locators import LogInLocators
from utils.usefull_elements import SignIn


class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(LogInLocators.URL)
        sleep(3)
        self.browser.find_element(*LogInLocators.accept_cookies_button).click()

    def type_email(self, username):
        self.browser.find_element(*LogInLocators.login_email_box).send_keys(username)

    def type_password(self, password):
        self.browser.find_element(*LogInLocators.login_password_box).send_keys(password)

    def click_sign_in(self):
        sleep(3)
        self.browser.find_element(*LogInLocators.login_button).click()

    def get_error_message(self, error_type):
        if error_type == "general_error":
            return self.browser.find_element(By.CSS_SELECTOR, "[class='sc-dlfnuX XGRlC']").text
        elif error_type == "username_error":
            return self.browser.find_element(By.CSS_SELECTOR, "div[data-type='email'] ["
                                                              "class='text-field__ErrorMessage-sc-1vll61a-4 "
                                                              "WGIUj']").text
        elif error_type == "password_error":
            return self.browser.find_element(By.CSS_SELECTOR, "div[data-type='password'] ["
                                                              "class='text-field__ErrorMessage-sc-1vll61a-4 "
                                                              "WGIUj']").text
