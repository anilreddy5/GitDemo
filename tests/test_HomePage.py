import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.submissionPage import submissionPage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    # def test_formSubmission(self):
    #     Submissionpage = submissionPage(self.driver)
    #     Submissionpage.getName().send_keys("Anil")
    #     # self.driver.find_element_by_name('name').send_keys('Anil')
    #     Submissionpage.getEmail().send_keys("anil@gmail.com")
    #     # self.driver.find_element_by_xpath("//input[@name='email']").send_keys("anil@gmail.com")
    #     Submissionpage.getPassword().send_keys("anil5")
    #     # self.driver.find_element_by_css_selector("input[@type='password']").send_keys("anil5")
    #     Submissionpage.getCheckBox().click()
    #     # self.driver.find_element_by_id("exampleCheck1").click()
    #     # sel = Select(Submissionpage.getGender())
    #     # sel = Select(self.driver.find_element_by_id("exampleFormControlSelect1"))
    #     self.selectGender(Submissionpage.getGender(), "Male")
    #     # sel.select_by_visible_text("Male")
    #     Submissionpage.getSubmit().click()
    #     # self.driver.find_element_by_xpath("//input[contains(@class, 'success')]").click()
    #     message = Submissionpage.getMessage().text
    #     # message = self.driver.find_element_by_css_selector("div[class*='dismiss']").text
    #     print(message)
    #     self.driver.get_screenshot_as_file("photo1.png")
    #     assert "success" in message
    #
    # the above code for just passing the keys manually
    # The below code is for how to call the data by using the Lists, Tuples and dictionaries

    def test_formSubmission(self, getData):
        log = self.getLogger()
        Submissionpage = submissionPage(self.driver)
        # Submissionpage.getName().send_keys(getData[0])
        # Submissionpage.getEmail().send_keys(getData[1])
        log.info("First name is " + getData["firstname"])
        Submissionpage.getName().send_keys(getData["firstname"])
        Submissionpage.getEmail().send_keys(getData["email"])
        Submissionpage.getPassword().send_keys("anil5")
        Submissionpage.getCheckBox().click()
        # self.selectGender(Submissionpage.getGender(), getData[2])
        self.selectGender(Submissionpage.getGender(), getData["gender"])
        Submissionpage.getSubmit().click()
        message = Submissionpage.getMessage().text
        print(message)
        self.driver.get_screenshot_as_file("photo1.png")
        print("Anil")
        assert "success" in message
        self.driver.refresh()
    # with tuples under list
    # @pytest.fixture(params=[("Anil", "anil@gmail.com", "Male"), ("chinni", "chinni@gmail.com", "Male")])
    # with dictionaries under list
    # @pytest.fixture(params=[{"firstname":"Anil", "email":"anil@gmail.com", "gender":"Male"}, {"firstname":"Chinni", "email":"chinni@gmail.com", "gender":"Female"}])
    # @pytest.fixture(params=HomePageData.test_data)
    @pytest.fixture(params=HomePageData.getTestData("TestCase4"))
    def getData(self, request):
        return request.param






