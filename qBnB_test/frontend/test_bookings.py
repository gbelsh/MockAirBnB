from seleniumbase import BaseCase
from qBnB_test.conftest import base_url


class bookListingTesting(BaseCase):

    # blackbox function requirements
    def test_requirements(self, *_):
        # Open the book Listing Page
        self.open(base_url + '/bookListing')

        # Book Listing Inputs
        self.type("#year", 2022)
        self.type("#month", 12)
        self.type("#day", 29)

        # Click Enter Button
        self.click('input[type="submit"]')

        # Upon successful Test
        self.open(base_url)
        # test if page loads
        
        self.assert_element("welcome-header")
        self.assert_element("Welcome John Cena!", "#welcome-header")

    def test_inputs_year(self, *_):
        # Testing booking page for year input that is not an integer
        self.open(base_url + '/bookListing')
        self.type("#year", "f")
        self.type("#month", 12)
        self.type("#day", 29)
        self.click('input[type="submit"]')

        msg = self.find_element('#message').text
        assert ("Listing Booking has failed" in msg)

        # Testing booking page for year input that is before 2021
        self.open(base_url + '/bookListing')
        self.type("#year", 2018)
        self.type("#month", 12)
        self.type("#day", 29)
        self.click('input[type="submit"]')

        msg = self.find_element('#message').text
        assert ("Listing Booking has failed" in msg)

    def test_inputs_month(self, *_):
        # Testing booking page for month input that is not an integer
        self.open(base_url + '/bookListing')
        self.type("#year", 2022)
        self.type("#month", "f")
        self.type("#day", 29)
        self.click('input[type="submit"]')

        msg = self.find_element('#message').text
        assert ("Listing Booking has failed" in msg)

        # Testing booking page for month input less then 1
        self.open(base_url + '/bookListing')
        self.type("#year", 2022)
        self.type("#month", 0)
        self.type("#day", 29)
        self.click('input[type="submit"]')

        msg = self.find_element('#message').text
        assert ("Listing Booking has failed" in msg)
    
        # Testing booking page for month input that is greater then 12
        self.open(base_url + '/bookListing')
        self.type("#year", 2022)
        self.type("#month", 13)
        self.type("#day", 29)
        self.click('input[type="submit"]')

        msg = self.find_element('#message').text
        assert ("Listing Booking has failed" in msg)

    def test_inputs_day(self, *_):
        # Testing booking page for day input that is not an integer
        self.open(base_url + '/bookListing')
        self.type("#year", 2022)
        self.type("#month", 12)
        self.type("#day", "f")
        self.click('input[type="submit"]')

        msg = self.find_element('#message').text
        assert ("Listing Booking has failed" in msg)

    def test_inputs_title(self, *_):
        # Testing booking page for a day input less then 1
        self.open(base_url + '/bookListing')
        self.type("#year", 2022)
        self.type("#month", 12)
        self.type("#day", 0)
        self.click('input[type="submit"]')

        msg = self.find_element('#message').text
        assert ("Listing Booking has failed" in msg)

        # Testing booking page for day input that is greater then 31
        self.open(base_url + '/bookListing')
        self.type("#year", 2022)
        self.type("#month", 12)
        self.type("#day", 32)
        self.click('input[type="submit"]')

        msg = self.find_element('#message').text
        assert ("Listing Booking has failed" in msg)