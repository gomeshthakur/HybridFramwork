import string
import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from selenium.webdriver.chrome.webdriver import Service
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from pageObjects.AddCustomer import addCustomer



class Test_003_Addcustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    def test_addcustomer(self):
        self.driver = webdriver.Chrome("C:\Program Files (x86)\Driver\chromedriver")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.page = Login(self.driver)
        self.page.setUserName(self.username)
        self.page.setPassword(self.password)
        self.page.clickLogin()

        self.addcust=addCustomer(self.driver)

        self.addcust.selectCustore()
        self.addcust.selectSubcustomer()
        self.addcust.AddButton()
        self.addcust.addemail("gt@mail.com")
        self.addcust.setPassword()
        self.addcust.setFirstName()
        self.addcust.setLastName()
        self.addcust.setGender()
        self.addcust.setDate()
        self.addcust.setCompany()
        self.addcust.setcheck()
