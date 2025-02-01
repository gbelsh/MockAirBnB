from seleniumbase import BaseCase
from qBnB_test.conftest import base_url


class ListingTesting(BaseCase):

    # Blackbox Functional Requirements
    def test_requirements(self, *_):
        # Open the Listing Creation Page
        self.open(base_url + '/listingPage')

        # Listing Inputs
        self.type("#title", "title")
        self.type("#description", "description is normal 20")
        self.type("#price", 11)

        # Click Enter Button
        self.click('input[type="submit"]')

        # Upon successful Test
        self.open(base_url)
        # test if homepage loads
        self.assert_element("welcome-header")
        self.assert_element("Welcome John Cena!", "#welcome-header")
    
    # Blackbox input testing
    def test_inputs_title(self, *_):
        # Testing Title Regex - /
        self.open(base_url + '/listingPage')
        self.type("#title", "/title")
        self.type("#description", "description is normal 20")
        self.type("#price", 11)
        self.click('input[type="submit"]')

        msg = self.find_element('#message').text
        assert ("Listing Creation Failed." in msg)

        # Testing Title Regex - 'space' in prefix
        self.open(base_url + '/listingPage')
        self.type("#title", " title")
        self.type("#description", "description is normal 20")
        self.type("#price", 11)
        self.click('input[type="submit"]')

        msg = self.find_element('#message').text
        assert ("Listing Creation Failed." in msg)

        # Testing Title Regex - 'space' in suffix
        self.open(base_url + '/listingPage')
        self.type("#title", "title ")
        self.type("#description", "description is normal 20")
        self.type("#price", 11)
        self.click('input[type="submit"]')

        msg = self.find_element('#message').text
        assert ("Listing Creation Failed." in msg)

        # Testing Title too Large
        self.open(base_url + '/listingPage')
        self.type("#title", "a" * 20)
        self.type("#description", "description is normal 20")
        self.type("#price", 11)
        self.click('input[type="submit"]')

        msg = self.find_element('#message').text
        assert ("Listing Creation Failed." in msg)

        # Testing Title duplicate
        self.open(base_url + '/listingPage')
        self.type("#title", "title")
        self.type("#description", "description is normal 20")
        self.type("#price", 11)
        self.click('input[type="submit"]')

        self.open(base_url + '/listingPage')
        self.type("#title", "title")
        self.type("#description", "description is normal 20")
        self.type("#price", 11)
        self.click('input[type="submit"]')

        msg = self.find_element('#message').text
        assert ("Listing Creation Failed." in msg)

        # Check if still on the same page
        self.wait(0.5)
        self.assert_element("#title")
        self.assert_element("#description")
        self.assert_element("#price")

    def test_inputs_description(self, *_):
        # Testing Description too small
        self.open(base_url + '/listingPage')
        self.type("#title", "title")
        self.type("#description", "description small")
        self.type("#price", 11)
        self.click('input[type="submit"]')

        msg = self.find_element('#message').text
        assert ("Listing Creation Failed." in msg)

        # Testing Description too large
        self.open(base_url + '/listingPage')
        self.type("#title", "title")
        self.type("#description", "description" * 2000)
        self.type("#price", 11)
        self.click('input[type="submit"]')

        msg = self.find_element('#message').text
        assert ("Listing Creation Failed." in msg)

        # Testing Description smaller than title
        self.open(base_url + '/listingPage')
        self.type("#title", "title is larger than\
            description for this test")
        self.type("#description", "description is normal 20")
        self.type("#price", 11)
        self.click('input[type="submit"]')

        msg = self.find_element('#message').text
        assert ("Listing Creation Failed." in msg)

        # Check if still on the same page
        self.wait(0.5)
        self.assert_element("#title")
        self.assert_element("#description")
        self.assert_element("#price")

    def test_inputs_price(self, *_):
        # Testing Price lower than 10
        self.open(base_url + '/listingPage')
        self.type("#title", "title")
        self.type("#description", "description is normal 20")
        self.type("#price", 9)
        self.click('input[type="submit"]')

        msg = self.find_element('#message').text
        assert ("Listing Creation Failed." in msg)

        # Testing Price higher than 10000
        self.open(base_url + '/listingPage')
        self.type("#title", "title")
        self.type("#description", "description is normal 20")
        self.type("#price", 10001)
        self.click('input[type="submit"]')

        msg = self.find_element('#message').text
        assert ("Listing Creation Failed." in msg)

        self.wait(0.5)
        self.assert_element("#title")
        self.assert_element("#description")
        self.assert_element("#price")
    
    def test_outputs(self, *_):
        # Listing Creation Failure
        self.open(base_url + '/listingPage')
        self.type("#title", "title")
        self.type("#description", "description is normal")
        self.type("#price", 9)
        self.click('input[type="submit"]')

        # Check if still on the same page
        self.wait(0.5)
        self.assert_element("#title")
        self.assert_element("#description")
        self.assert_element("#price")

        # Listing Creation Successful
        self.open(base_url + '/listingPage')
        self.type("#title", "title")
        self.type("#description", "description is normal")
        self.type("#price", 11)
        self.click('input[type="submit"]')
