from seleniumbase import BaseCase
from qBnB_test.conftest import base_url


class RegistrationTesting(BaseCase):

    # Blackbox Functional Requirements
    def test_requirements(self, *_):
        # Open the registration page
        self.open(base_url + '/registerPage')

        # Registration Inputs
        self.type("#email", "reqEmail@test.com")
        self.type("#username", "John Cena")
        self.type("#password", "ReqPass123#")
        self.type("#password2", "ReqPass123#")

        # Click Enter Button
        self.click('input[type="submit"]')

        # Open login page
        self.open(base_url + '/loginPage')
        # Input email and password
        self.type("#email", "reqEmail@test.com")
        self.type("#password", "ReqPass123#")

        # Click Enter Button
        self.click('input[type="submit"]')

        # If test is successful,
        self.open(base_url)
        # test if the page loads correctly
        self.assert_element("#welcome-header")
        self.assert_element("Welcome John Cena!",
                            "#welcome-header")

    # Blackbox Input Partitioning
    def test_inputs_email(self, *_):
        # Testing Email - Regex Test
        self.open(base_url + '/registerPage')
        self.type("#email", "emailtest1@test@tester.com")
        self.type("#username", "Jimin")
        self.type("#password", "emailTest123#")
        self.type("#password2", "emailTest123#")
        self.click('input[type="submit"]')

        msg = self.find_element('#message').text
        assert ("Registration failed." in msg)

        # Testing Email - No Email Input
        self.open(base_url + '/registerPage')
        self.type("#email", "")
        self.type("#username", "Jimin")
        self.type("#password", "emailTest123#")
        self.type("#password2", "emailTest123#")
        self.click('input[type="submit"]')

        msg = self.find_element('#message').text
        assert ("Registration failed." in msg)

        # Testing Email - email duplicates
        self.open(base_url + '/registerPage')
        self.type("#email", "emailtest3@test.com")
        self.type("#username", "Jimin")
        self.type("#password", "emailTest123#")
        self.type("#password2", "emailTest123#")
        self.click('input[type="submit"]')

        self.open(base_url + '/registerPage')
        self.type("#email", "emailtest3@test.com")
        self.type("#username", "Jungkook")
        self.type("#password", "emailTest123#")
        self.type("#password2", "emailTest123#")
        self.click('input[type="submit"]')

        msg = self.find_element('#message').text
        assert ("Registration failed." in msg)

        # Check if still on the same page
        self.wait(0.5)
        self.assert_element("#email")
        self.assert_element("#username")
        self.assert_element("#password")
        self.assert_element("#password2")

    def test_inputs_username(self, *_):
        # Testing Username - space in prefix
        self.open(base_url + '/registerPage')
        self.type("#email", "untest1@test.com")
        self.type("#username", " Jimin")
        self.type("#password", "unTest123#")
        self.type("#password2", "unTest123#")
        self.click('input[type="submit"]')

        msg = self.find_element('#message').text
        assert ("Registration failed." in msg)

        # Testing Username - space in suffix
        self.open(base_url + '/registerPage')
        self.type("#email", "untest2@test.com")
        self.type("#username", "Jimin ")
        self.type("#password", "unTest123#")
        self.type("#password2", "unTest123#")
        self.click('input[type="submit"]')

        msg = self.find_element('#message').text
        assert ("Registration failed." in msg)

        # Testing Username - Special Characters
        self.open(base_url + '/registerPage')
        self.type("#email", "untest3@test.com")
        self.type("#username", "Jimin!@#")
        self.type("#password", "unTest123#")
        self.type("#password2", "unTest123#")
        self.click('input[type="submit"]')

        msg = self.find_element('#message').text
        assert ("Registration failed." in msg)

        # Testing Username - Less than 2 chars
        self.open(base_url + '/registerPage')
        self.type("#email", "untest1@test.com")
        self.type("#username", "J")
        self.type("#password", "unTest123#")
        self.type("#password2", "unTest123#")
        self.click('input[type="submit"]')

        msg = self.find_element('#message').text
        assert ("Registration failed." in msg)

        # Testing Username - too many chars (>20)
        self.open(base_url + '/registerPage')
        self.type("#email", "untest1@test.com")
        self.type("#username",
                  "JiminIsTheGreatestKpopStarOfAllTime")
        self.type("#password", "unTest123#")
        self.type("#password2", "unTest123#")
        self.click('input[type="submit"]')

        msg = self.find_element('#message').text
        assert ("Registration failed." in msg)

        # Testing Username - Empty Input
        self.open(base_url + '/registerPage')
        self.type("#email", "untest1@test.com")
        self.type("#username", "")
        self.type("#password", "unTest123#")
        self.type("#password2", "unTest123#")
        self.click('input[type="submit"]')

        msg = self.find_element('#message').text
        assert ("Registration failed." in msg)

        # Check if still on the same page
        self.wait(0.5)
        self.assert_element("#email")
        self.assert_element("#username")
        self.assert_element("#password")
        self.assert_element("#password2")

    def test_inputs_password(self, *_):
        # Testing Password - 1 Special Char
        self.open(base_url + '/registerPage')
        self.type("#email", "pswdtest1@test.com")
        self.type("#username", "Jimin")
        self.type("#password", "emailTest123")
        self.type("#password2", "emailTest123")
        self.click('input[type="submit"]')

        msg = self.find_element('#message').text
        assert ("Registration failed." in msg)

        # Testing Password - 1 lower case
        self.open(base_url + '/registerPage')
        self.type("#email", "pswdtest2@test.com")
        self.type("#username", "Jimin")
        self.type("#password", "EMAILTEST123#")
        self.type("#password2", "EMAILTEST123#")
        self.click('input[type="submit"]')

        msg = self.find_element('#message').text
        assert ("Registration failed." in msg)

        # Testing Password - 1 upper case
        self.open(base_url + '/registerPage')
        self.type("#email", "pswdtest3@test.com")
        self.type("#username", "Jimin")
        self.type("#password", "emailtest123#")
        self.type("#password2", "emailtest123#")
        self.click('input[type="submit"]')

        msg = self.find_element('#message').text
        assert ("Registration failed." in msg)

        # Testing Password - Less than 6 Chars
        self.open(base_url + '/registerPage')
        self.type("#email", "pswdtest4@test.com")
        self.type("#username", "Jimin")
        self.type("#password", "Em1#")
        self.type("#password2", "Em1#")
        self.click('input[type="submit"]')

        msg = self.find_element('#message').text
        assert ("Registration failed." in msg)

        # Testing Password - Empty Password
        self.open(base_url + '/registerPage')
        self.type("#email", "pswdtest1@test.com")
        self.type("#username", "Jimin")
        self.type("#password", "")
        self.type("#password2", "")
        self.click('input[type="submit"]')

        msg = self.find_element('#message').text
        assert ("Registration failed." in msg)

        # Check if still on the same page
        self.wait(0.5)
        self.assert_element("#email")
        self.assert_element("#username")
        self.assert_element("#password")
        self.assert_element("#password2")

    # Blackbox Output Partitioning
    def test_outputs(self, *_):
        # Registration Failure
        self.open(base_url + "/registerPage")
        self.type("#email", "outputTest1@test.com")
        self.type("#name", "John Cena")
        self.type("#password", "outPass123")
        self.type("#password2", "outPass123")
        self.click('input[type="submit"]')

        # Check if still on the same page
        self.wait(0.5)
        self.assert_element("#email")
        self.assert_element("#name")
        self.assert_element("#password")
        self.assert_element("#password2")

        # Registration was Successful
        self.open(base_url + "/registerPage")
        self.type("#email", "outputTest2@test.com")
        self.type("#name", "John Cena")
        self.type("#password", "outPass123#")
        self.type("#password2", "outPass123#")
        self.click('input[type="submit"]')
