import pytest
from selenium import webdriver
from PageObject.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customerLogger import LogGen

class Test_001_Login:
    baseurl = ReadConfig.getApplication()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    log = LogGen.loggen()

    def test_HomePageTitle(self, setup):
        self.log.info("this is Test_001_Login")
        self.log.info("this is home page title test")
        self.driver = setup
        self.driver.get(self.baseurl)
        act_title = "Your store. Login"

        if act_title == self.driver.title:
            assert True
            self.driver.close()
            self.log.info("home page title test is passed")

        else:
            self.driver.get_screenshot_as_file(".\\Screenshots\\pic.png")
            self.driver.close()
            self.log.error("home page title test is failed")
            assert False

    def test_Login(self, setup):
        self.log.info("this is home page login test")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        act_title = "Dashboard / nopCommerce administration"

        if act_title == self.driver.title:
            assert True
            self.driver.close()
            self.log.info("home page login test is passed")

        else:
            self.driver.get_screenshot_as_file(".\\Screenshots\\LoginPage.png")
            self.driver.close()
            self.log.info("home page login test is failed")
            assert False






















