from selenium.webdriver.common.by import By


class SearchCustomer:
    ### Add customer Page

    txt_email_id = "SearchEmail"
    txt_fname_id = "SearchFirstName"
    txt_lname_id = "SearchLastName"
    btn_search_id = "search-customers"

    # tbl_SearchResult_xpath = ""
    table_xpath = '//*[@id="customers-grid"]'
    table_row_xpath = '//*[@id="customers-grid"]/tbody/tr'
    table_column_xpath = '//*[@id="customers-grid"]/tbody/tr/td'

    def __init__(self, driver):
        self.driver = driver

    def setemail(self, email):
        self.driver.find_element(By.ID, self.txt_email_id).clear()
        self.driver.find_element(By.ID, self.txt_email_id).send_keys(email)

    def setfirstname(self, fname):
        self.driver.find_element(By.ID, self.txt_fname_id).clear()
        self.driver.find_element(By.ID, self.txt_fname_id).send_keys(fname)

    def setlastname(self, lname):
        self.driver.find_element(By.ID, self.txt_lname_id).clear()
        self.driver.find_element(By.ID, self.txt_lname_id).send_keys(lname)

    def clicksearch(self):
        self.driver.find_element(By.ID, self.btn_search_id).click()

    def get_NoOfRows(self):
        return len(self.driver.find_elements(By.XPATH, self.table_row_xpath))

    def get_NoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH, self.table_column_xpath))

    def SearchCustomerByEmail(self, email):
        flag = False
        for r in range(1, self.get_NoOfRows()+1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            emailid = table.find_element(By.XPATH, '//*[@id="customers-grid"]/tbody/tr["+str(r)+"]/td[2]').text

            if emailid == email:
                flag = True
                break

        return flag

    def SearchCustomerByName(self, Name):
        flag = False
        for r in range(1, self.get_NoOfColumns() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            name = table.find_element(By.XPATH, '//*[@id="customers-grid"]/tbody/tr["+str(r)+"]/td[3]').text

            if name == Name:
                flag = True
                break

        return flag




























