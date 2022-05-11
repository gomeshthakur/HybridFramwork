import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver


class addCustomer():
    lnk_customer_xpath="//a[@href='#']//p[contains(text(),'Customers')]"
    lnk_subcustomer_xpath="//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btn_addnew_xpath="//a[normalize-space()='Add new']"
    txt_email_xpath="//input[@id='Email']"
    txt_password_xpath="//input[@id='Password']"
    txt_firstname_xpath="//input[@id='FirstName']"
    txt_lastname_xpath="//input[@id='LastName']"
    rad_gender_xpath="//input[@class='form-check-input']"
    rad_male_xpath="//input[@id='Gender_Male']"
    rad_female_xpath="//input[@id='Gender_Female']"
    txt_date_xpath="//input[@id='DateOfBirth']"
    txt_company_xpath="//input[@id='Company']"
    chk_tax_xpath="//input[@id='IsTaxExempt']"
    txt_news_xpath="//div[@class='input-group-append']//div[@role='listbox']"
    lst_customer_xpath="//div[@class='input-group-append input-group-required']//div[@role='listbox']"
    drp_vendor_xpath="//select[@id='VendorId']"
    chk_active_xpath="//input[@id='Active']"
    txt_comment_xpath="//textarea[@id='AdminComment']"
    btn_save_xpath="//button[@name='save']"


    def __init__(self,driver):
        self.driver=driver

    def selectCustore(self):
        self.driver.find_element_by_xpath(self.lnk_customer_xpath).click()

    def selectSubcustomer(self):
        self.driver.find_element_by_xpath(self.lnk_subcustomer_xpath).click()

    def AddButton(self):
        self.driver.find_element_by_xpath(self.btn_addnew_xpath).click()

    def addemail(self):
        self.driver.find_element_by_xpath(self.txt_email_xpath).send_keys()

    def setPassword(self):
        self.driver.find_element_by_xpath(self.txt_password_xpath).send_keys()

    def setFirstName(self):
        self.driver.find_element_by_xpath(self.txt_firstname_xpath).send_keys()

    def setLastName(self):
        self.driver.find_element_by_xpath(self.txt_lastname_xpath).send_keys()

    def setGender(self,gender):
        if gender=="Male":
            self.driver.find_element_by_xpath(self.rad_male_xpath).click()

        elif gender=="Female":
            self.driver.find_element_by_xpath(self.rad_female_xpath).click()

        else:
            self.driver.find_element_by_xpath(self.rad_male_xpath).click()

    def setDate(self):
        self.driver.find_element_by_xpath(self.txt_date_xpath).send_keys()

    def setCompany(self):
        self.driver.find_element_by_xpath(self.txt_company_xpath).send_keys()

    def setcheck(self):
        self.driver.find_element_by_xpath(self.chk_tax_xpath).click()

    def setNews(self):
        self.driver.find_element_by_xpath(self.txt_news_xpath).send_keys()

    def setVendor(self):
        drpdown=Select(self.driver.find_element_by_xpath(self.drp_vendor_xpath))
        drpdown.select_by_visible_text()

    def clkSave(self):
        self.driver.find_element_by_xpath(self.btn_save_xpath).click()
