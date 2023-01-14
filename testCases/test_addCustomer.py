import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from PageObject.LoginPage import LoginPage
from PageObject.AddCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customerLogger import LogGen
import string
import random


class Test_003_AddCustomer:
    baseurl = ReadConfig.getApplication()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    log = LogGen.loggen()


    def test_addcustomer(self,setup):
        self.log.info("*** Test_003_AddCustomer ***")
        self.driver = setup
        self.driver.get(self.baseurl)

        self.lp = LoginPage(self.driver)
        self.lp = LoginPage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        self.log.info("login is Successfully done")
        self.log.info("start to add customer")

        self.Addcust = AddCustomer(self.driver)
        self.Addcust.click_customer_menu()
        self.Addcust.click_customer_menuitem()

        self.Addcust.click_Addnew_Button()
        self.email = random_generator() + "@gmail.com"
        self.Addcust.setEmailId(self.email)
        self.Addcust.setpassword('test123')
        self.Addcust.set_Firstname_id('Rahul')
        self.Addcust.set_Lastname_id('Pande')
        self.Addcust.set_gender('male')
        self.Addcust.set_dob('5/27/1995')
        self.Addcust.set_Companyname('TCS')
        self.Addcust.set_customerrole('Guests')
        self.Addcust.set_mang_vendor('Vendor 2')
        self.Addcust.set_admincomment("this is adding customer test")
        self.Addcust.set_save()

        self.log.info("saving customer info")
        self.log.info("Add customer validation started")

        self.msg = self.driver.find_element(By.TAG_NAME, 'body').text
        print(self.msg)

        if "The new customer has been added successfully." in self.msg:
            assert True == True
            self.log.info("Add customer Test passed")

        else:
            self.log.error("Add customer test failed")
            assert True == False

        self.driver.close()
        self.log.info("ending Add customer test")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))






























