import time

import pytest
from PageObject.LoginPage import LoginPage
from PageObject.AddCustomerPage import AddCustomer
from PageObject.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customerLogger import LogGen


class Test_SearchCustomerByEmail_004:
    baseurl = ReadConfig.getApplication()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    log = LogGen.loggen()

    def test_SearchCustomerByEmail(self, setup):
        self.log.info("SearchCustomerByEmail_004")
        self.driver = setup
        self.driver.get(self.baseurl)

        self.lp = LoginPage(self.driver)
        self.lp = LoginPage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        self.log.info("login is Successfully done")
        self.log.info("starting search customer by email")

        self.Addcust = AddCustomer(self.driver)
        self.Addcust.click_customer_menu()
        self.Addcust.click_customer_menuitem()

        self.log.info(" search customer by emailiD")
        self.searchcust = SearchCustomer(self.driver)
        self.searchcust.setemail("victoria_victoria@nopCommerce.com")
        self.searchcust.clicksearch()
        time.sleep(3)

        status = self.searchcust.SearchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert True == status
        self.log.info("TC_SearchCustomerByEmail_004 finished")
        self.driver.close()


































