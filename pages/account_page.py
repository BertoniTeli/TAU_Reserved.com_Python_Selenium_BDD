from time import sleep

from locators.locators import AccountPageLocators


class AccountPageBody:
    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(AccountPageLocators.URL)
        sleep(3)
        self.browser.find_element(*AccountPageLocators.accept_cookies_button).click()

    def click_order_history_button(self):
        self.browser.find_element(*AccountPageLocators.order_history_button).click()

    def click_return_list_button(self):
        self.browser.find_element(*AccountPageLocators.return_list_button).click()

    def click_edit_account_button(self):
        self.browser.find_element(*AccountPageLocators.edit_account_button).click()

    def click_address_data_button(self):
        self.browser.find_element(*AccountPageLocators.address_data_button).click()

    def click_invoice_data_button(self):
        self.browser.find_element(*AccountPageLocators.invoice_data_button).click()

    def click_logout_button(self):
        self.browser.find_element(*AccountPageLocators.logout_button).click()
