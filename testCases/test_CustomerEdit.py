import string
import time
import pytest

from selenium.webdriver.common.by import By

from pageObject.LoginPage import LoginPage
from pageObject.addcustomerPage import AddCustomer
from pageObject.CustomerEdit import EditCustomers
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import  random


class Test_015_EditCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_editCustomer(self,setup):
        self.logger.info("*********** Test_015 ***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********** Login Succesfull ***********")

        self.logger.info("********** Starting Editing Customer ***********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.editcust = EditCustomers(self.driver)
        time.sleep(3)
        self.editcust.clickOnSearchBtn()
        time.sleep(3)
        self.editcust.clickOnCustEdit()
        time.sleep(3)
        self.logger.info("******** Providing Customer Details *********")

        self.editcust.clickOnCustEmail("Nandu@gmail.com")
        self.editcust.clickOnCustFname("Nandu")
        self.editcust.clickOnCustLname("Kumar")
        self.editcust.clickOnCustCname("Msys")
        self.editcust.clickOnCustomerEdit_Save()

        self.logger.info("************* Saving customer info **********")

        self.logger.info("********* Add customer validation started *****************")

        self.msg = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissable']").text

        print(self.msg)

        if 'The customer has been updated successfully.' in self.msg:
            assert True
            self.logger.info("********* Edit Customer Test Passed **********")

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_EditCustomer_scr.png")  # Screenshot
            self.logger.error("********* Edit customer Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("*********** Ending Editing Customer Test *************")

    def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))