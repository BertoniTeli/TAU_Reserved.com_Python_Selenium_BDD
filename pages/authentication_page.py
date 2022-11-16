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

    def box_email_sign_in(self):
        self.browser.find_element(*LogInLocators.login_email_box).send_keys(SignIn.TEST_ACCOUNT)

    def box_email_sign_in_unsuccessfully(self, username):
        if username == "\\":
            username = ""
        self.browser.find_element(*LogInLocators.login_email_box).send_keys(username)

    def box_password_sign_in(self):
        self.browser.find_element(*LogInLocators.login_password_box).send_keys(SignIn.TEST_PASSWORD)

    def box_password_sign_in_unsuccessfully(self, password):
        if password == "\\":
            password = ""
        self.browser.find_element(*LogInLocators.login_password_box).send_keys(password)

    def click_sign_in(self):
        self.browser.find_element(*LogInLocators.login_button).click()

    def set_user_inputs(self):
        self.browser.find_element(*LogInLocators.login_email_box).send_keys("testDaniel@yahoo.com")
        self.browser.find_element(*LogInLocators.login_password_box).send_keys("123456")
        self.browser.find_element(*LogInLocators.login_button).click()

    def return_error_message(self):

        center_error = self.browser.find_element(LogInLocators.center_error_message)
        error_list_a = [center_error]
        email_error = self.browser.find_element(LogInLocators.email_error_message)
        error_list_b = [email_error]
        password_error = self.browser.find_element(LogInLocators.password_error_message)
        error_list_c = [password_error]

        if len(error_list_a) != 0:
            center_error = self.browser.find_element(By.CSS_SELECTOR, "[.sc-dlfnuX]").get_attribute("explicit-name")
            return center_error
        elif len(error_list_b) != 0:
            email_error = self.browser.find_element(By.LINK_TEXT, "Vă rugăm să introduceți numai caractere valide").text
            return email_error
        elif len(error_list_c) != 0:
            password_error = self.browser.find_element(By.XPATH, "/html//form/div[2]/div/div").get_attribute(
                "innerHTML")
            return password_error
        else:
            return "No error displayed"
