import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from selenium.webdriver.chrome.webdriver import Service
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from Utilities import XLUtils


import threading
# @pytest.mark.usefixtures("setup")
class Test_Login_02_DDT:
    baseURL=ReadConfig.getApplicationURL()
    path="D:\\pythonProject\\HybridFramwork\\TestData\\testData.xlsx"
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
    def test_login_DDT(self):
        self.driver = webdriver.Chrome("C:\Program Files (x86)\Driver\chromedriver")
        # self.driver=setup
        self.driver.get(self.baseURL)

        self.page=Login(self.driver)

        self.rows=XLUtils.getRowCount(self.path,'Sheet1')
        print(self.rows)

        # for r in range(2,self.rows+1):
        self.user=XLUtils.readData(self.path,'Sheet1',2,1)
        self.password = XLUtils.readData(self.path, 'Sheet1', 2, 2)



        self.page.setUserName(self.user)
        self.page.setPassword(self.password)
        self.page.clickLogin()
        # title=self.driver.title
        # print(title)
        # if title=="Dashboard / nopCommerce administration11":
        #     assert True
        #     print("Test Case Is Passed")
        # else:
        #     self.driver.save_screenshot("D:\pythonProject\HybridFramwork\Screenshots\testlogin6.png")
        #     self.driver.close()