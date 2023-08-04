import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObject.LoginPage import LoginPage
from pageObject.Export import ExportCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


@pytest.mark.data2
class Test_ExportCustomerExcelAll_010:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    def test_export(self, setup):
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

        self.export = ExportCustomer(self.driver)
        self.export.clickOnCustomerMenu()
        self.export.clickOnCustomers_MenuItem()

        self.logger.info("************* Exporting Customer Detail Test Started *****************")

        self.export.clickOnDropdownButton_Export()
        self.export.clickOnExportToExcel_all()
        time.sleep(8)

        self.logger.info("***************** Exporting Customer Excel all ********************")

        # self.driver.close()
        self.logger.info("******* Ending Export customer test **********")

        assert True
