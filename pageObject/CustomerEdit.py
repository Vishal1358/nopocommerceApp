from selenium.webdriver.common.by import By


class EditCustomers:
    iconSearch_click_btn_xpath = "//div/div[@class='icon-collapse']"
    CustomerEdit_Xpath1 = "//tbody/tr[@class='odd']//td/a[@href='Edit/5']"
    # CustomerEdit_Xpath2 = "//tbody/tr/td/a[@href='Edit/155']"
    CustomerEdit_Email_xpath = "//input[@id='Email']"
    CustomerEdit_Fname_xpath = "//input[@id='FirstName']"
    CustomerEdit_Lname_xpath = "//input[@id='LastName']"
    CustomerEdit_Cpname_xpath = "//input[@id='Company']"
    CustomerEdit_and_Save = "//div/button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnSearchBtn(self):
        self.driver.find_element(By.XPATH,self.iconSearch_click_btn_xpath).click()

    def clickOnCustEdit(self):
        self.driver.find_element(By.XPATH, self.CustomerEdit_Xpath1).click()

    def clickOnCustEmail(self, email):
        self.driver.find_element(By.XPATH, self.CustomerEdit_Email_xpath).clear()
        self.driver.find_element(By.XPATH, self.CustomerEdit_Email_xpath).send_keys(email)

    def clickOnCustFname(self, Fname):
        self.driver.find_element(By.XPATH, self.CustomerEdit_Fname_xpath).clear()
        self.driver.find_element(By.XPATH, self.CustomerEdit_Fname_xpath).send_keys(Fname)

    def clickOnCustLname(self, Lname):
        self.driver.find_element(By.XPATH, self.CustomerEdit_Lname_xpath).clear()
        self.driver.find_element(By.XPATH, self.CustomerEdit_Lname_xpath).send_keys(Lname)

    def clickOnCustCname(self, Cname):
        self.driver.find_element(By.XPATH, self.CustomerEdit_Cpname_xpath).clear()
        self.driver.find_element(By.XPATH, self.CustomerEdit_Cpname_xpath).send_keys(Cname)

    def clickOnCustomerEdit_Save(self):
        self.driver.find_element(By.XPATH, self.CustomerEdit_and_Save).click()
