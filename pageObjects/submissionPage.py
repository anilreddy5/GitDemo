from selenium.webdriver.common.by import By


class submissionPage:

    def __init__(self, driver):
        self.driver = driver
    name = (By.NAME, "name")
    email = (By.XPATH, "//input[@name='email']")
    password = (By.XPATH, "//input[@type='password']")
    checkBox = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    genderSelect = (By.XPATH, "//input[contains(@class, 'success')]")
    submit = (By.XPATH, "//input[contains(@class, 'success')]")
    message = (By.CSS_SELECTOR, "div[class*='dismiss']")

    def getName(self):
        return self.driver.find_element(*submissionPage.name)

    def getEmail(self):
        return self.driver.find_element(*submissionPage.email)

    def getPassword(self):
        return self.driver.find_element(*submissionPage.password)

    def getCheckBox(self):
        return self.driver.find_element(*submissionPage.checkBox)

    def getGender(self):
        return self.driver.find_element(*submissionPage.gender)

    def getGenderSelect(self):
        return self.driver.find_element(*submissionPage.genderSelect)

    def getSubmit(self):
        return self.driver.find_element(*submissionPage.submit)

    def getMessage(self):
        return self.driver.find_element(*submissionPage.message)