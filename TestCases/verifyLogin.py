from Pages.login import *


class VerifyLogin():
    @staticmethod
    def executeLogin():
        try:
            loginPage = LoginPage()
            loginPage.login()
        except Exception as error:
            print(error)
