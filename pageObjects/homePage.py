from selenium.webdriver.common.by import By

from pageObjects.checkOutPage import checkOutPage


class HomePage:
    # define constructor
    def __init__(self, driver):
        self.driver = driver
    shop = (By.LINK_TEXT, "Shop")

    def shopItems(self):
        # return self.driver.find_element(*HomePage.shop)
        self.driver.find_element(*HomePage.shop).click()
        Checkoutpage = checkOutPage(self.driver)
        return Checkoutpage

# If it is a class variable, we need to call the defined object by classname.object, in this case homePage.shop
# if it is a instance variable in the constructor, we need to call the object by self.object
# by passing the *, it will identify the Tuple

