from DriverSetup import browser
from CommonMethods.commonMethods import ReusableMethods as use


class LoginPage:
    @staticmethod
    def login():
        # Get the Submit Button
        globalBrowser = browser.getBrowser()
        submitBTN = globalBrowser.find_element(by="id", value="login-button")

        # get the username and password list
        usernameText = (globalBrowser.find_element(by="id", value="login_credentials")).text
        usernameList = usernameText.splitlines()
        passwordText = (globalBrowser.find_element(by="class name", value="login_password")).text
        passwordList = passwordText.splitlines()

        # call to method with placeholder and value
        use.setvalue('Username', usernameList[1])
        use.setvalue('Password', passwordList[1])

        #  Click Login
        submitBTN.click()
