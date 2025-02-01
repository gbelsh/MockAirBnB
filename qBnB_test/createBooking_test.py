from qBnB.backend import bookListing
from qBnB.models import db, Listing, User, Booking
from uuid import uuid4
from datetime import date
import datetime as dt


# Create test users
user1 = User(
    user_id='123345678',
    email='test@test.com',
    username='user 00',
    password='87654321',
    billing_address='101 union St',
    postal_code='K7L2J8',
    balance=100)
db.session.add(user1)
db.session.commit()

user2 = User(
    user_id='123345678910',
    email='test3@test.com',
    username='user 02',
    password='87654321',
    billing_address='101 union St',
    postal_code='K7L2J8',
    balance=100)
db.session.add(user2)
db.session.commit()

# Create test listings
newListing = Listing(
    id='123345678', title='aaaaaaaaaaa',
    description='description is normal 20',
    price=11,
    last_modified_date=dt.datetime(2022, 9, 13),
    owner_id='1111111')
db.session.add(newListing)
db.session.commit()

newListing2 = Listing(
    id='123345678910', title='bbbbbbbbbbb',
    description='description is normal 20',
    price=11,
    last_modified_date=dt.datetime(2022, 9, 13),
    owner_id='2222222')
db.session.add(newListing2)
db.session.commit()


# Create test booking
newBooking = Booking(
    id='123124124',
    user_id='123345678', 
    listing_id='1111111', 
    price=11,
    date=dt.datetime(2022, 12, 28))
db.session.add(newBooking)
db.session.commit()


def test_r6_1_create_booking():
    """
    Testing R6_1: A user can book a listing.
    """   
    assert bookListing(newListing.owner_id, user1.user_id, "2022",
                       "12", "25") is True
    
    
def test_r6_2_create_booking():
    """
    Testing R6_1: A user cannot book a listing for his/her listing.
    """   
    assert bookListing(newListing.owner_id, newListing.id, "2022", 
                       "12", "26") is False
    
    
def test_r6_3_create_booking():
    """
    Testing R6_1: A user cannot book a listing that costs more than 
    his/her balance.
    """   
    assert bookListing(newListing.owner_id, user2.user_id, "2022", 
                       "12", "27") is False
    
    
def test_r6_4_create_booking():
    """
    Testing R6_1: A user cannot book a listing that is already 
    booked with the overlapped dates.
    """   
    assert bookListing(newBooking.listing_id, user2.user_id, "2022", 
                       "12", "28") is False