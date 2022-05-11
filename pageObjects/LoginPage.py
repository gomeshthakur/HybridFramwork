from selenium import webdriver

class Login:
    text_username_id="Email"
    text_password_id="Password"
    btn_login_xpath="//button[normalize-space()='Log in']"

    def __init__(self,driver):
        self.driver=driver

    def setUserName(self,username):
        self.driver.find_element_by_id(self.text_username_id).clear()
        self.driver.find_element_by_id(self.text_username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element_by_id(self.text_password_id).clear()
        self.driver.find_element_by_id(self.text_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.btn_login_xpath).click()