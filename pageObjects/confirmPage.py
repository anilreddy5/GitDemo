from selenium.webdriver.common.by import By


class confirmPage:
    def __init__(self, driver):
        self.driver = driver

    country = (By.ID, "country")
    selectCountry = (By.LINK_TEXT, "India")
    clickCheckBox = (By.CSS_SELECTOR, "[for=checkbox2]")
    purchase = (By.CSS_SELECTOR, "[type='submit']")
    message = (By.CLASS_NAME, "alert-success")

    def getCountry(self):
        return self.driver.find_element(*confirmPage.country)

    def getSelectCountry(self):
        return self.driver.find_element(*confirmPage.selectCountry)

    def checkBox(self):
        return self.driver.find_element(*confirmPage.clickCheckBox)

    def purchaseClick(self):
        return self.driver.find_element(*confirmPage.purchase)

    def successMessage(self):
        return self.driver.find_element(*confirmPage.message)