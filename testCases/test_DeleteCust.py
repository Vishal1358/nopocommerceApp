import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObject.DeleteCust import DeleteCustomer
from pageObject.LoginPage import LoginPage
from pageObject.Export import ExportCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


@pytest.mark.sanity
class Test_Delete_Customer_016:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    def test_Delete(self, setup):
        self.logger.info("************* Export  **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("************* Exporting Customer By Email *****************")

        self.delete = DeleteCustomer(self.driver)
        self.delete.clickOnCustomerMenu()
        time.sleep(2)
        self.delete.clickOnCustomers_MenuItem()
        time.sleep(2)
        self.logger.info("********** Deleting Process **********")

        self.delete.clickOnIcon_Collapse()
        time.sleep(2)
        self.delete.clickOn_lnkCustomers_edit()
        time.sleep(2)
        self.delete.clickOn_lnkCustomers_delete()
        time.sleep(2)
        assert True
