import pytest
from selenium import webdriver
# to give the knowledge to the screenshot browser use the global driver so that all the driver objects use the same browser
driver = None

# @pytest.fixture(scope='class')
# def setup(request): # this fixture is to invoke the browser and also for the code simplification purposes, we can call this fixture directly before a test case or more
#     driver = webdriver.Chrome(executable_path='C:\\Users\\ANIL\\selenium\\chromedriver_win32\\chromedriver.exe')
#     driver.maximize_window()
#     driver.get("https://rahulshettyacademy.com/angularpractice/")
#     request.cls.driver = driver
#     yield
#     driver.quit()
    # return driver
    # when we have yield statement return statement does not work, in this case we need to pass the request instance

# Command Line option to select the browser

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope='class')
def setup(request):
    global driver
    browserName = request.config.getoption("--browser_name") # this config is used for browser instances
    if browserName == "chrome":
        driver = webdriver.Chrome(executable_path='C:\\Users\\ANIL\\selenium\\chromedriver_win32\\chromedriver.exe')
    elif browserName == "firefox":
        driver = webdriver.Chrome(executable_path='C:\\Users\\ANIL\\selenium\\geckodriver-v0.26.0-win32\\geckodriver.exe')
    elif browserName == "IE":
        driver = webdriver.Chrome(executable_path='C:\\Users\\ANIL\\selenium\\geckodriver-v0.26.0-win32\\MicrosoftWebDriver.exe')
        print("IE Browser")
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver
    yield
    driver.quit()
# the command for to run in different browsers is py.test --browser_name chrome
# if you run with the py.test only, the default browser will invoke

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)
