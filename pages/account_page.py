from selenium.webdriver.common.by import By

from locators.locators import LogInLocators
from pages.authentication_page import LoginPage


class LogiPage:
    def __init__(self, browser):
        self.browser = browser

    def safa(self):
        self.browser.get(LogInLocators.URL)
        error3 = self.browser.find_element(By.CSS_SELECTOR, ".sc-dlfnuX").get_attribute("innerHTML")
        error = LoginPage.find_error_message
        print(error, error3)


def test_fasdf(browser):
    LogiPage(browser).safa()

    #          pip install pipenv
    #          pipenv install selenium
    #          pipenv install webdriver_manager
    #          pipenv install pytest
    #          pipenv install pytest_bdd
"""
print(error)
    if browser.find_element(By.XPATH, "/html//form/div[2]/div/div").is_displayed():
        password_error = browser.find_element(By.XPATH, "/html//form/div[2]/div/div").get_attribute('innerHTML')
        print(password_error)
        assert password_error == error
    elif browser.find_element(By.CSS_SELECTOR, ".sc-dlfnuX").is_displayed():
        center_error = browser.find_element(By.CSS_SELECTOR, ".sc-dlfnuX").get_attribute('innerHTML')
        print(center_error)
        print("a executat 2")
        assert center_error == error
    else:
        email_error = browser.find_element(By.XPATH, "/html//form/div[1]/div/div").get_attribute('innerHTML')
        print(email_error)
        assert email_error == error
"""