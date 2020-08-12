from BaseApp import BasePage
from selenium.webdriver.common.by import By

class FBSeacrhLocators:
    LOCATOR_FB_EMAIL = (By.ID, "email")
    LOCATOR_FB_PASSW = (By.ID, "pass")
    LOCATOR_FB_EBUTTON = (By.CLASS_NAME, "_6ltg")
    LOCATOR_FB_AFTERLOG = (By.CLASS_NAME, "_5v-0 _53in")

class SearchHelper(BasePage):

    def enter_email(self, email):
        email_field = self.find_element(FBSeacrhLocators.LOCATOR_FB_EMAIL)
        email_field.click()
        email_field.send_keys(email)
        return email_field

    def enter_passw(self, passw):
        passw_field = self.find_element(FBSeacrhLocators.LOCATOR_FB_PASSW)
        passw_field.click()
        passw_field.send_keys(passw)
        return passw_field

    def click_on_the_enter_button(self):
        return self.find_element(FBSeacrhLocators.LOCATOR_FB_EBUTTON,time=2).click()

    def check_login(self):
        log_field = self.find_elements(FBSeacrhLocators.LOCATOR_FB_AFTERLOG,time=2)
        content = [x.text for x in log_field if len(x.text) > 0]
        return content