from seleniumbase import BaseCase

from qBnB_test.conftest import base_url

"""
This file defines all integration tests for the frontend
UpdateUserProfile page.
"""


class FrontEndUpdateUserProfileTest(BaseCase):

    # Blackbox Functional Requirements
    def test_requirements(self, *_):
        # Navigate to /updateProfile
        self.open(base_url + '/updateProfile')

        # Fill inputs
        self.type("#username", "test user")
        self.type("#email", "test@test.com")
        self.type("#billingAddress", "101 Union St")
        self.type("#postalCode", "K7L2J8")

        # Click submit button
        self.click('input[type="submit"]')

        # Navigate to homepage
        self.open(base_url)

        # test if username was updated correctly
        self.assert_element("#welcome-header")
        self.assert_text("Welcome test user!", "#welcome-header")

    # Blackbox Input Partitioning
    def test_inputs_username(self, *_):
        # Testing username - no input
        self.open(base_url + '/updateProfile')
        self.type("#username", "")
        self.type("#email", "test@test.com")
        self.type("#billingAddress", "101 Union St")
        self.type("#postalCode", "K7L2J8")
        self.click('input[type="submit"]')

        msg = self.find_element('#message').text
        assert ("Invalid Username" in msg)

        # Test username - less than 2 chars
        self.open(base_url + '/updateProfile')
        self.type("#username", "t")
        self.type("#email", "test@test.com")
        self.type("#billingAddress", "101 Union St")
        self.type("#postalCode", "K7L2J8")
        self.click('input[type="submit"]')

        msg = self.find_element('#message').text
        assert ("Invalid Username" in msg)

        # Test username - more than 20 chars
        self.open(base_url + '/updateProfile')
        self.type("#username", "testusertestusertestuser")
        self.type("#email", "test@test.com")
        self.type("#billingAddress", "101 Union St")
        self.type("#postalCode", "K7L2J8")
        self.click('input[type="submit"]')

        msg = self.find_element('#message').text
        assert ("Invalid Username" in msg)

        # Test username - Special chars
        self.open(base_url + '/updateProfile')
        self.type("#username", "")
        self.type("#email", "test@test.com")
        self.type("#billingAddress", "101 Union St")
        self.type("#postalCode", "K7L2J8")
        self.click('input[type="submit"]')

        msg = self.find_element('#message').text
        assert ("Invalid Username" in msg)

        # Test username - space in prefix
        self.open(base_url + '/updateProfile')
        self.type("#username", " testuser")
        self.type("#email", "test@test.com")
        self.type("#billingAddress", "101 Union St")
        self.type("#postalCode", "K7L2J8")
        self.click('input[type="submit"]')

        msg = self.find_element('#message').text
        assert ("Invalid Username" in msg)

        # Test username - space in suffix
        self.open(base_url + '/updateProfile')
        self.type("#username", "testuser ")
        self.type("#email", "test@test.com")
        self.type("#billingAddress", "101 Union St")
        self.type("#postalCode", "K7L2J8")
        self.click('input[type="submit"]')

        msg = self.find_element('#message').text
        assert ("Invalid Username" in msg)

        # Check if still on the same page
        self.wait(0.5)
        self.assert_element("#email")
        self.assert_element("#username")
        self.assert_element("#billingAddress")
        self.assert_element("#postalCode")

    def test_input_email(self, *_):
        # Testing email - regex
        self.open(base_url + '/updateProfile')
        self.type("#username", "testuser")
        self.type("#email", "test@test@tester.com")
        self.type("#billingAddress", "101 Union St")
        self.type("#postalCode", "K7L2J8")
        self.click('input[type="submit"]')

        msg = self.find_element('#message').text
        assert ("Invalid Email" in msg)

        # Testing email - no input
        self.open(base_url + '/updateProfile')
        self.type("#username", "testuser")
        self.type("#email", "test@test@tester.com")
        self.type("#billingAddress", "101 Union St")
        self.type("#postalCode", "K7L2J8")
        self.click('input[type="submit"]')

        msg = self.find_element('#message').text
        assert ("Invalid Email" in msg)

        # Check if still on the same page
        self.wait(0.5)
        self.assert_element("#email")
        self.assert_element("#username")
        self.assert_element("#billingAddress")
        self.assert_element("#postalCode")

    def test_input_postal_code(self, *_):
        # Testing postal code - no input
        self.open(base_url + '/updateProfile')
        self.type("#username", "testuser")
        self.type("#email", "test@test.com")
        self.type("#billingAddress", "101 Union St")
        self.type("#postalCode", "")
        self.click('input[type="submit"]')

        msg = self.find_element('#message').text
        assert ("Invalid Postal Code" in msg)

        # Testing postal code - regex
        self.open(base_url + '/updateProfile')
        self.type("#username", "testuser")
        self.type("#email", "test@test.com")
        self.type("#billingAddress", "101 Union St")
        self.type("#postalCode", "F7L2J8")
        self.click('input[type="submit"]')

        msg = self.find_element('#message').text
        assert ("Invalid Postal Code" in msg)

        # Testing postal code - special chars
        self.open(base_url + '/updateProfile')
        self.type("#username", "testuser")
        self.type("#email", "test@test.com")
        self.type("#billingAddress", "101 Union St")
        self.type("#postalCode", "K7!2J8")
        self.click('input[type="submit"]')

        msg = self.find_element('#message').text
        assert ("Invalid Postal Code" in msg)

        # Check if still on the same page
        self.wait(0.5)
        self.assert_element("#email")
        self.assert_element("#username")
        self.assert_element("#billingAddress")
        self.assert_element("#postalCode")

    # Blackbox Output Partitioning
    def test_outputs(self, *_):
        # username failure
        self.open(base_url + '/updateProfile')
        self.type("#username", "testuser ")
        self.type("#email", "test@test.com")
        self.type("#billingAddress", "101 Union St")
        self.type("#postalCode", "K7L2J8")
        self.click('input[type="submit"]')

        msg = self.find_element('#message').text
        assert ("Invalid Username" in msg)

        # Check if still on the same page
        self.wait(0.5)
        self.assert_element("#email")
        self.assert_element("#username")
        self.assert_element("#billingAddress")
        self.assert_element("#postalCode")

        # email failure
        self.open(base_url + '/updateProfile')
        self.type("#username", "testuser")
        self.type("#email", "test@test@tester.com")
        self.type("#billingAddress", "101 Union St")
        self.type("#postalCode", "K7L2J8")
        self.click('input[type="submit"]')

        msg = self.find_element('#message').text
        assert ("Invalid Email" in msg)

        # Check if still on the same page
        self.wait(0.5)
        self.assert_element("#email")
        self.assert_element("#username")
        self.assert_element("#billingAddress")
        self.assert_element("#postalCode")

        # Postal Code Failure
        self.open(base_url + '/updateProfile')
        self.type("#username", "testuser")
        self.type("#email", "test@test.com")
        self.type("#billingAddress", "101 Union St")
        self.type("#postalCode", "F7L2J8")
        self.click('input[type="submit"]')

        msg = self.find_element('#message').text
        assert ("Invalid Postal Code" in msg)

        # Check if still on the same page
        self.wait(0.5)
        self.assert_element("#email")
        self.assert_element("#username")
        self.assert_element("#billingAddress")
        self.assert_element("#postalCode")

        # Successful update
        self.open(base_url + '/updateProfile')
        self.type("#username", "test user")
        self.type("#email", "test@test.com")
        self.type("#billingAddress", "101 Union St")
        self.type("#postalCode", "K7L2J8")
        self.click('input[type="submit"]')
        self.open(base_url)

        self.assert_element("#welcome-header")
        self.assert_text("Welcome test user!", "#welcome-header")
