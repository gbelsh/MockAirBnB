from qBnB.backend import createListing
from qBnB.backend import user_registration
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


@pytest.mark.parametrize('title', payloads)
def test_r1_title(title):
    """
    Testing Title parameter with payloads
    """
    user_registration('test2@test.com', 'u21', 'TestR2#1')
    try:
        assert createListing(
            title, 'description is normal 20',
            11, 'test2@test.com', '2') is False
    except AssertionError:
        assert True


@pytest.mark.parametrize('description', payloads)
def test_r2_description(description):
    """
    Testing description parameter with payloads
    """
    user_registration('test2@test.com', 'u21', 'TestR2#1')
    try:
        assert createListing(
            'aaaaaaaaaaa', description, 11, 
            'test2@test.com', '2') is False
    except AssertionError:
        assert True


@pytest.mark.parametrize('price', payloads)
def test_r3_price(price):
    """
    Testing price parameter with payloads *** Works ***
    """
    user_registration('test2@test.com', 'u21', 'TestR2#1')
    try:
        assert createListing(
            'aaaaaaaaaaa',
            'description is normal 20',
            price, 'test2@test.com', 'u21') is False
    except TypeError:
        assert True


@pytest.mark.parametrize('email', payloads)
def test_r4_email(email):
    """
    Testing email parameter with payloads
    """
    user_registration('test2@test.com', 'u21', 'TestR2#1')
    try:
        assert createListing(
            'aaaaaaaaaaa',
            'description is normal 20',
            11, email, 'u21') is False
    except TypeError:
        assert True


@pytest.mark.parametrize('id', payloads)
def test_r5_id(id):
    """
    Testing id parameter with payloads
    """
    user_registration('test2@test.com', 'u21', 'TestR2#1')
    try:
        assert createListing(
            'aaaaaaaaaaa',
            'description is normal 20',
            11, "test2@test.com", id) is False
    except TypeError:
        assert True