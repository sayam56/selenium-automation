import time
from DriverSetup import browser
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from DriverSetup import browser as Driver


class ReusableMethods:

    @staticmethod
    def setvalue(label, value, ):
        getBrowser = browser.getBrowser()
        locator = "//input[@placeholder='" + label + "']"
        locatorTB = getBrowser.find_element(by="xpath", value=locator)

        locatorTB.send_keys(value)
        time.sleep(1)

    @staticmethod
    def logout():
        getBrowser = browser.getBrowser()
        # expand the hamburger menu
        menuBTN = getBrowser.find_element(by="id", value="react-burger-menu-btn")
        menuBTN.click()

        time.sleep(1.5)

        # Get the logout button and click logout
        logoutBTN = getBrowser.find_element(by="id", value="logout_sidebar_link")
        wait = WebDriverWait(getBrowser, 5).until(EC.element_to_be_clickable(logoutBTN))
        wait.click()
