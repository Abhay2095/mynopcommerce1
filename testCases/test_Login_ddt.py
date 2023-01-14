import time

import pytest
from selenium import webdriver
from PageObject.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customerLogger import LogGen
from utilities import XLUtils

class Test_002_DDT_Login:
    baseurl = ReadConfig.getApplication()
    path = ".\\TestData\\LoginData.xlsx"
    log = LogGen.loggen()


    def test_Login_ddt(self, setup):
        self.log.info("this is Test_002_DDT_Login")
        self.log.info("this is home page login test")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print(self.rows)
        lst_status = []
        for r in range(2, self.rows+1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setusername(self.user)
            self.lp.setpassword(self.password)
            self.lp.clicklogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.log.info("****passed***")
                    self.lp.clicklogout()
                    lst_status.append("Pass")

                elif self.exp == "Fail":
                    self.log.info("****Failed***")
                    self.lp.clicklogout()
                    lst_status.append("Fail")

            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.log.info("****Failed***")
                    lst_status.append("Fail")

                elif self.exp == "Fail":
                    self.log.info("**** Passed ***")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.log.info("Login DDT Test Passed....")
            self.driver.close()
            assert True

        else:
            self.log.info("Login DDT Test Failed....")
            self.driver.close()
            assert False

        self.log.info("******* End of Login DDT Test *****")
        self.log.info("*** Completed TC_LoginDDT_002 ***")








































































