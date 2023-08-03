from selenium.webdriver.common.by import By


class DeleteCustomer:
    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']"
    icon_collapse_xpath = "//div[@class='icon-collapse']"
    lnkCustomers_edit_xpath = "//td/a[@href='Edit/6']"
    # lnkCustomers_edit_xpath = "//td/a[@href='Edit/4']"
    lnkCustomers_delete_xpath = "//div/span[@id='customer-delete']"
    lnkCustomers_delete_done_xpath = "//button[contains(text(),'Delete')]"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menu_xpath).click()

    def clickOnCustomers_MenuItem(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menuitem_xpath).click()

    def clickOnIcon_Collapse(self):
        self.driver.find_element(By.XPATH, self.icon_collapse_xpath).click()

    def clickOn_lnkCustomers_edit(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_edit_xpath).click()

    def clickOn_lnkCustomers_delete(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_delete_xpath).click()

    def clickOn_lnkCustomers_done_delete(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_delete_done_xpath).click()
