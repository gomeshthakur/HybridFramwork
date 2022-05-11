import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from selenium.webdriver.chrome.webdriver import Service
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen



import threading
# @pytest.mark.usefixtures("setup")
class Test_Login_01:
    baseURL=ReadConfig.getApplicationURL()
    username= ReadConfig.getUserName()
    password= ReadConfig.getPassword()

    log = LogGen.loggen()

    def test_homepageTitle(self):
        self.log.info("********** Test Case 01 **********************")
        self.log.info("####### Verify Homepage ##############")

        self.driver=webdriver.Chrome("C:\Program Files (x86)\Driver\chromedriver")
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        # self.driver.close()
        if act_title=="Your store. Login":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("D:\pythonProject\HybridFramwork\Screenshots\testlogin.png")
            assert False
    def test_login(self):
        self.driver = webdriver.Chrome("C:\Program Files (x86)\Driver\chromedriver")
        # self.driver=setup
        self.driver.get(self.baseURL)

        self.page=Login(self.driver)
        self.page.setUserName(self.username)
        self.page.setPassword(self.password)
        self.page.clickLogin()
        title=self.driver.title
        print(title)
        if title=="Dashboard / nopCommerce administration11":
            assert True
            print("Test Case Is Passed")
        else:
            self.driver.save_screenshot("D:\pythonProject\HybridFramwork\Screenshots\testlogin6.png")
            self.driver.close()