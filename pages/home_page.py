from time import sleep
from selenium.webdriver.common.by import By

from locators.locators import LogInLocators
from utils.usefull_elements import SignIn


class HomePage:
    def __init__(self, browser):
        self.browser = browser

    def get_account_name(self):
        return self.browser.find_element(By.CSS_SELECTOR, "[data-testid='account-info-logged-true']").text
