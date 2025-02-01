from seleniumbase import BaseCase
from qBnB_test.conftest import base_url
from qBnB.backend import user_registration


class LoginTesting(BaseCase):

    # Blackbox Functional Requirements
    def test_login_requirements(self, *_):

        user_registration("reqTest@test.com",
                          "reqUser", "ReqPass123#")

        self.open(base_url + '/loginPage')
        self.type("#email", "reqTest@test.com")
        self.type("#password", "ReqPass123#")
        self.click('input[type="submit"]')

        self.assert_element("#welcome-header")
        self.assert_element("Welcome reqUser!",
                            "#welcome-header")

    def test_login_inputs(self, *_):
        # Blackbox Input Partitioning

        user_registration("in1Test@test.com",
                          "inUser", "inPass123#")

        # Incorrect email, Incorrect Password
        self.open(base_url + '/loginPage')
        self.type("#email", "intest@test.com")
        self.type("#password", "innPass123#")
        self.click('input[type="submit"]')

        msg = self.find_element('#message').text
        assert ("login failed" in msg)

        # Incorrect email, Correct Password
        self.open(base_url + '/loginPage')
        self.type("#email", "intest@test.com")
        self.type("#password", "inPass123#")
        self.click('input[type="submit"]')

        msg = self.find_element('#message').text
        assert ("login failed" in msg)

        # Correct email, Incorrect Password
        self.open(base_url + '/loginPage')
        self.type("#email", "in1Test@test.com")
        self.type("#password", "innPass123#")
        self.click('input[type="submit"]')

        msg = self.find_element('#message').text
        assert ("login failed" in msg)

    def test_login_outputs(self, *_):
        # Blackbox Output Partitioning

        user_registration("out1Test@test.com",
                          "outUser", "outPass123#")

        # Failed Login
        self.open(base_url + '/loginPage')
        self.type("#email", "outtest@test.com")
        self.type("#password", "outPasss123#")
        self.click('input[type="submit"]')

        msg = self.find_element('#message').text
        assert ("login failed" in msg)

        # Successful Login
        self.open(base_url + '/loginPage')
        self.type("#email", "out1Test@test.com")
        self.type("#password", "outPass123#")
        self.click('input[type="submit"]')

        self.assert_element("#welcome-header")
        self.assert_text("Welcome outUser!",
                         "#welcome-header")
