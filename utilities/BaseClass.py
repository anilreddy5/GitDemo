import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures('setup')
class BaseClass():

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger

    def verifyLinkPresence(self, text):
        wait = WebDriverWait(self.driver, 7)
        # wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def selectGender(self, locator, text):
        # sel = Select(Submissionpage.getGender())
        sel = Select(locator)
        sel.select_by_visible_text("Male")

# Instead of avtual text, we can call it as text argument then it works for all the text elements by calling with actual text in the actual test case
    # pass
# pass is the keyword, just to say we are not doing anything here
# Here baseclass has the knowledge of setup fixture
#