import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.checkOutPage import checkOutPage
from pageObjects.confirmPage import confirmPage
from pageObjects.homePage import HomePage
from utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        nameList = ['Blackberry']
        cartList = []
        homePage = HomePage(self.driver)
        # homePage.shopItems().click()
        Checkoutpage = homePage.shopItems()
        # here we can use driver in two ways one is passing the setup fixture into test case and also by defining request.cls.driver = driver then to self.driver
        # you can only access the class driver is with the self
        # carts = self.driver.find_element_by_css_selector(".card-title a")
        # Checkoutpage = checkOutPage(self.driver)
        carts = Checkoutpage.getCarts()
        i = -1
        for cart in carts:
            i = i + 1
            # name = cart.find_element_by_xpath("//div//h4//a")[i].text
            name = cart.text
            log.info(name)
            print(name)
            if name == "Blackberry":
                # cart.find_elements_by_xpath("div//button").click()
                Checkoutpage.getCardFooter()[i].click()
        # self.driver.find_element_by_css_selector(".btn-primary").click()
        Checkoutpage.goToCheckOutButton().click()
        # items = self.driver.find_elements_by_xpath("//div[@class='media']//div//h4//a")
        items = Checkoutpage.getItems()
        for item in items:
            cartList.append(item.text)
        print(cartList)
        log.info(cartList)

        assert nameList == cartList

        # self.driver.find_element_by_css_selector(".btn-success").click()
        # Checkoutpage.clickOnCheckOut().click()
        Confirmpage = Checkoutpage.clickOnCheckOut()
        # self.driver.find_element_by_id("country").send_keys("Ind")
        # Confirmpage = confirmPage(self.driver)
        log.info("Passing the keyword as Ind ")
        Confirmpage.getCountry().send_keys("Ind")
        # wait = WebDriverWait(self.driver, 7)
        # wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.verifyLinkPresence("India")
        # self.driver.find_element_by_link_text("India").click()
        Confirmpage.getSelectCountry().click()
        # self.driver.find_element_by_css_selector("[for=checkbox2]").click()
        Confirmpage.checkBox().click()
        # self.driver.find_element_by_css_selector("[type='submit']").click()
        Confirmpage.purchaseClick().click()
        # successMessage = self.driver.find_element_by_class_name("alert-success").text
        successMessage = Confirmpage.successMessage().text
        print(successMessage)
        log.info("Success message will be " + successMessage)
        assert "Success!" in successMessage

        self.driver.get_screenshot_as_file("photo.png")

    def test_e2e2(self):
        log = self.getLogger()
        nameList = ['Blackberry']
        cartList = []
        homePage = HomePage(self.driver)

    def test_e2e3(self):
        log = self.getLogger()
        nameList = ['Blackberry']
        cartList = []
        homePage = HomePage(self.driver)