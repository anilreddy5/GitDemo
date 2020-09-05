from selenium.webdriver.common.by import By

from pageObjects.confirmPage import confirmPage


class checkOutPage:

    def __init__(self, driver):
        self.driver = driver
    carts = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    checkOutButton1 = (By.CSS_SELECTOR, ".btn-primary")
    items = (By.XPATH, "//div[@class='media']//div//h4//a")
    checkOutButton2 = (By.CSS_SELECTOR, ".btn-success")
    def getCarts(self):
        return self.driver.find_elements(*checkOutPage.carts)

    def getCardFooter(self):
        return self.driver.find_elements(*checkOutPage.cardFooter)

    def goToCheckOutButton(self):
        return self.driver.find_element(*checkOutPage.checkOutButton1)

    def getItems(self):
        return self.driver.find_elements(*checkOutPage.items)

    def clickOnCheckOut(self):
        # return self.driver.find_element(*checkOutPage.checkOutButton2)
        self.driver.find_element(*checkOutPage.checkOutButton2).click()
        Confirmpage = confirmPage(self.driver)
        return Confirmpage
