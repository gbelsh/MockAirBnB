from qBnB.backend import user_registration
import pytest


with open("payloads.txt") as i: 
    with open("payloadsSecure.txt", "w") as o:
        for payload in i: 
            o.write("'%s'\n" % payload[:-1])


payloadFile = open('payloadsSecure.txt', 'r')
payloads = payloadFile.read().splitlines()


@pytest.mark.parametrize('email', payloads)
def test_r1_email(email):
    """
    Testing email parameter with payloads
    """
    try:
        assert user_registration(
            email, 'u21', 
            'TestR2#1') is False
    except AssertionError:
        assert True


@pytest.mark.parametrize('username', payloads)
def test_r2_username(username):
    """
    Testing username parameter with payloads
    """
    try:
        assert user_registration(
            'test2@test.com', 
            username, 'TestR2#1') is False
    except AssertionError:
        assert True


@pytest.mark.parametrize('password', payloads)
def test_r3_password(password):
    """
    Testing password parameter with payloads
    """
    try:
        assert user_registration(
            'test2@test.com', 
            'u21', password) is False
    except AssertionError:
        assert True