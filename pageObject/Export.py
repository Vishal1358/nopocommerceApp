from selenium.webdriver.common.by import By


class ExportCustomer:
    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']"
    tblMainCheckbox1_xpath = "//tbody/tr/td/input[@value=6]"
    # tblMainCheckbox2_xpath = "/tbody/tr/td/input[@value=5]"
    # tblMainCheckbox3_xpath = "/tbody/tr/td/input[@value=4]"
    # tblMainCheckbox4_xpath = "/tbody/tr/td/input[@value=3]"
    dropdownButton_Export_xpath = "//div[@class='btn-group']//button[@data-toggle='dropdown']"
    exportToXML_All = "//ul/li/button[@name='exportxml-all']"
    exportToXML_Selected = "//ul/li/button[@id='exportxml-selected']"
    exportToExcel_all = "//ul/li/button[@name='exportexcel-all']"
    exportToExcel_Selected = "//ul/li/button[@id='exportexcel-selected']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menu_xpath).click()

    def clickOnCustomers_MenuItem(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menuitem_xpath).click()

    def clickOnMainCheckbox1(self):
        self.driver.find_element(By.XPATH, self.tblMainCheckbox1_xpath).click()
        # self.driver.find_element(By.XPATH, self.tblMainCheckbox2_xpath).click()

    def clickOnMainCheckbox2(self):
        self.driver.find_element(By.XPATH, self.tblMainCheckbox1_xpath).click()
        # self.driver.find_element(By.XPATH, self.tblMainCheckbox3_xpath).click()
        # self.driver.find_element(By.XPATH, self.tblMainCheckbox4_xpath).click()

    def clickOnDropdownButton_Export(self):
        self.driver.find_element(By.XPATH, self.dropdownButton_Export_xpath).click()

    def clickOnExportToXML_All(self):
        self.driver.find_element(By.XPATH, self.exportToXML_All).click()

    def clickOnExportToXML_Selected(self):
        self.driver.find_element(By.XPATH, self.exportToXML_Selected).click()

    def clickOnExportToExcel_all(self):
        self.driver.find_element(By.XPATH, self.exportToExcel_all).click()

    def clickOnExportToExcel_Selected(self):
        self.driver.find_element(By.XPATH, self.exportToExcel_Selected).click()
