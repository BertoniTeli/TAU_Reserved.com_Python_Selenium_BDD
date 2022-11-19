from time import sleep

from selenium.webdriver.common.by import By

from locators.locators import AccountPageLocators


class AccountPageBody:
    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(AccountPageLocators.URL)
        sleep(3)
        self.browser.find_element(*AccountPageLocators.accept_cookies_button).click()

    def enter_account_menu(self):
        self.browser.find_element(*AccountPageLocators.account_menu).click()
        sleep(3)
        self.browser.find_element(*AccountPageLocators.close_newsletter_popup_button).click()

    def get_account_name(self):
        self.browser.find_element(*AccountPageLocators.account_menu).text()

    def click_account_menu_buttons(self, button):
        if button == "Comenzile mele":
            self.browser.find_element(*AccountPageLocators.order_history_button).click()
            print("\nClick!")
        elif button == "Retururile mele":
            self.browser.find_element(*AccountPageLocators.return_list_button).click()
            print("\nClick!")
        elif button == "Setările contului":
            self.browser.find_element(*AccountPageLocators.edit_account_button).click()
            print("\nClick!")
        elif button == "Adrese de livrare":
            self.browser.find_element(*AccountPageLocators.address_data_button).click()
            print("\nClick!")
        elif button == "Adresă de facturare":
            self.browser.find_element(*AccountPageLocators.invoice_data_button).click()
        elif button == "Delogare":
            self.browser.find_element(*AccountPageLocators.logout_button).click()

    def get_button_name(self, button):
        self.browser.find_element(By.LINK_TEXT, f"{button}").get_attribute("innerHTML")
    """
    def get_order_history_button_name(self):
        self.browser.find_element(*AccountPageLocators.order_history_button).click()

    def get_return_list_button_name(self):
        self.browser.find_element(*AccountPageLocators.return_list_button).click()

    def get_edit_account_button_name(self):
        self.browser.find_element(*AccountPageLocators.edit_account_button).click()

    def get_address_data_button_name(self):
        self.browser.find_element(*AccountPageLocators.address_data_button).click()

    def get_invoice_data_button_name(self):
        self.browser.find_element(*AccountPageLocators.invoice_data_button).click()

    def get_logout_button_name(self):
        self.browser.find_element(*AccountPageLocators.logout_button).click()
    """
    def get_account_menu_buttons_name(self, button):
        if button == "Comenzile mele":
            return self.browser.find_element(*AccountPageLocators.order_history_button).text
        elif button == "Retururile mele":
            return self.browser.find_element(*AccountPageLocators.return_list_button).text
        elif button == "Setările contului":
            return self.browser.find_element(*AccountPageLocators.edit_account_button_bug).text
        elif button == "Adrese de livrare":
            return self.browser.find_element(*AccountPageLocators.address_data_button_bug).text
        elif button == "Adresă de facturare":
            return self.browser.find_element(*AccountPageLocators.invoice_data_button_bug).text
        elif button == "Delogare":
            return self.browser.find_element(*AccountPageLocators.logout_button).text
