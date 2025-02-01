from qBnB.models import db, Listing, User
from qBnB.backend import bookListing
import datetime as dt
import pytest


# Used to concatenate payloads will be 
# added to to code structure after sprint
with open("payloads.txt") as i: 
    with open("payloadsSecure.txt", "w") as o:
        for payload in i: 
            o.write("'%s'\n" % payload[:-1]) 
            # writing to new file inverted as without
            # inversion file would have reverse payloads


payloadFile = open('payloadsSecure.txt', 'r')
payloads = payloadFile.read().splitlines()

test_user = User(
    user_id='123345678',
    email='test@test.com',
    username='user 00',
    password='87654321',
    billing_address='101 union St',
    postal_code='K7L2J8',
    balance=100)
db.session.add(test_user)
test_listing = Listing(
    id='123345678', title='aaaaaaaaaaa',
    description='description is normal 20',
    price=11,
    last_modified_date=dt.datetime(2022, 9, 13),
    owner_id='1111111')
db.session.add(test_listing)


@pytest.mark.parametrize('listId', payloads)
def test_r1_listId(listId):
    """
    Testing listID parameter with payloads
    """    
    try:
        assert bookListing(
            listId, '123345678', 
            2022, 9, 13) is False
    except AttributeError:
        assert True


@pytest.mark.parametrize('ownerId', payloads)
def test_r2_description(ownerId):
    """
    Testing ownerID parameter with payloads
    """
    try:
        assert bookListing(
            '1111111', ownerId, 
            2022, 9, 13) is False
    except AttributeError:
        assert True


@pytest.mark.parametrize('year', payloads)
def test_r3_price(year):
    """
    Testing year parameter with payloads *** Works ***
    """
    try:
        assert bookListing(
            '1111111', '123345678', 
            year, 9, 13) is False
    except ValueError:
        assert True


@pytest.mark.parametrize('month', payloads)
def test_r4_email(month):
    """
    Testing month parameter with payloads
    """
    try:
        assert bookListing(
            '1111111', '123345678', 
            2022, month, 13) is False
    except ValueError:
        assert True


@pytest.mark.parametrize('day', payloads)
def test_r5_id(day):
    """
    Testing day parameter with payloads
    """
    try:
        assert bookListing(
            '1111111', '123345678', 
            2022, 9, day) is False
    except ValueError:
        assert True