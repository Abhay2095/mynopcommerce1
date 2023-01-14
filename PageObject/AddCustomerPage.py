import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCustomer:
    txt_customer_menu_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a/p"
    txt_customer_menuitem_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p"
    btn_Addnew_xpath = "/html/body/div[3]/div[1]/form[1]/div/div/a"
    txt_email_id = "Email"
    txt_password_id = "Password"
    txt_fname_id = "FirstName"
    txt_lname_id = "LastName"
    rb_male_id = "Gender_Male"
    rb_female_id = "Gender_Female"
    txt_dob_id = "DateOfBirth"
    txt_companyname_id = "Company"
    txt_customerRole_xpath = '//*[@id="customer-info"]/div[2]/div[10]/div[2]/div/div[1]/div/div'
    txt_Administrators_xpath = "//li[normalize-space()='Administrators']"
    txt_Guests_xpath = "//li[normalize-space()='Guests']"
    txt_Registered_xpath = "//li[normalize-space()='Registered']"
    txt_Vendors_xpath = "//li[contains(text(),'Vendors')]"
    drp_mngofvendor_id = "VendorId"
    txt_admincomment_id = "AdminComment"
    btn_save_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def click_customer_menu(self):
        self.driver.find_element(By.XPATH, self.txt_customer_menu_xpath).click()

    def click_customer_menuitem(self):
        self.driver.find_element(By.XPATH, self.txt_customer_menuitem_xpath).click()

    def click_Addnew_Button(self):
        self.driver.find_element(By.XPATH, self.btn_Addnew_xpath).click()

    def setEmailId(self, email):
        self.driver.find_element(By.ID, self.txt_email_id).send_keys(email)

    def setpassword(self, password):
        self.driver.find_element(By.ID, self.txt_password_id).send_keys(password)

    def set_Firstname_id(self, fname):
        self.driver.find_element(By.ID, self.txt_fname_id).send_keys(fname)

    def set_Lastname_id(self, lname):
        self.driver.find_element(By.ID, self.txt_lname_id).send_keys(lname)

    def set_gender(self, gender):
        if gender == 'male':
            self.driver.find_element(By.ID, self.rb_male_id).click()

        elif gender == 'female':
            self.driver.find_element(By.ID, self.rb_female_id).click()

        else:
            self.driver.find_element(By.ID, self.rb_male_id).click()

    def set_dob(self, dob):
        self.driver.find_element(By.ID, self.txt_dob_id).send_keys(dob)

    def set_Companyname(self, comname):
        self.driver.find_element(By.ID, self.txt_companyname_id).send_keys(comname)

    def set_customerrole(self, role):

        self.driver.find_element(By.XPATH, self.txt_customerRole_xpath).click()
        time.sleep(3)

        if role == 'Administrators':
            self.driver.find_element(By.XPATH, self.txt_customerRole_xpath).click()
            time.sleep(3)
            self.driver.find_element(By.XPATH, self.txt_Administrators_xpath).click()

        elif role == 'Guests':
            time.sleep(3)
            self.driver.find_element(By.XPATH, "//span[@title='delete']").click()

            time.sleep(3)
            self.driver.find_element(By.XPATH, self.txt_customerRole_xpath).click()

            time.sleep(3)
            self.driver.find_element(By.XPATH, self.txt_Guests_xpath).click()


        elif role == "Vendors":
            self.driver.find_element(By.XPATH, self.txt_customerRole_xpath).click()
            time.sleep(3)
            self.driver.find_element(By.XPATH, self.txt_Vendors_xpath).click()

        else:
            self.driver.find_element(By.XPATH, self.txt_Guests_xpath).click()



    def set_mang_vendor(self, value):
        drp = Select(self.driver.find_element(By.ID, self.drp_mngofvendor_id))
        drp.select_by_visible_text(value)

    def set_admincomment(self, comment):
        self.driver.find_element(By.ID, self.txt_admincomment_id).send_keys(comment)

    def set_save(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()






































