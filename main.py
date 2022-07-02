from DriverSetup import browser
from TestCases.verifyDashboard import VerifyDashboard
from TestCases.verifyLogin import VerifyLogin
import time

url = "https://www.saucedemo.com/"


# Driver Setup
browser.initBrowser()
browser.goto(url)
time.sleep(1.5)

# execute test cases
loginCase = VerifyLogin().executeLogin()
dashBoardCase = VerifyDashboard().executeDash()
logoutCase = VerifyDashboard().executeLogout()

time.sleep(1.5)

browser.closeBrowser()

