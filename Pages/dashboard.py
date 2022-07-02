from DriverSetup import browser
from CommonMethods.commonMethods import ReusableMethods as use


class DashboardPage:
    @staticmethod
    def verifyDashCase():
        getBrowser = browser.getBrowser()
        # this is an element variable
        dashText = (getBrowser.find_element(by="class name", value="title")).text
        if dashText.lower() == 'products':
            pass
        else:
            print(dashText)

    @staticmethod
    def verifyLogoutCase():
        use.logout()



