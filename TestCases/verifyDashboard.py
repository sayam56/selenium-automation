from Pages.dashboard import *


class VerifyDashboard:

    @staticmethod
    def executeDash():
        try:
            DashboardPage().verifyDashCase()
        except Exception as error:
            print(error)

    @staticmethod
    def executeLogout():
        try:
            DashboardPage().verifyLogoutCase()
        except Exception as error:
            print(error)
