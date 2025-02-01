from datetime import datetime
from qBnB.backend import createListing, price_Check
from qBnB.backend import descriptionCheck, titleCheck
from qBnB.backend import last_modified_dateCheck
from qBnB.backend import title_description_Check
from qBnB.backend import user_registration


def test_r4_1_a_create_Listing():
    """
    Testing R1-1-a: Title doesn't meet regex requirements
    """
    assert titleCheck(
        '/aaaaaaaaaaa{') is False
    assert titleCheck(
        'aaaaaaaaaaa') is True


def test_r4_1_b_create_Listing():
    """
    Testing R1-1-b: Title has space in suffix or prefix
    """
    assert titleCheck(
        ' aaaaaaaaaa') is False
    assert titleCheck(
        'aaaaaaaaaaa ') is False
    assert titleCheck(
        'aaaaaaaaaaaaaaa') is True


def test_r4_2_create_Listing():
    """
    Testing R4-2: Title size cannot be larger than 80 characters
    """
    assert titleCheck(
        'aaaaaaaaaaaaaaaaaaaaaaaaaa' +
        'aaaaaaaaaaaaaaaaaaaaaaaaaa' +
        'aaaaaaaaaaaaaaaaaaaaaaaaaa' +
        'aaaaaaaaaaa') is False
    assert titleCheck(
        'aaaaaaaaaaa') is True


def test_r4_3_create_Listing():
    """
    Testing R4-3: Description size cannot be smaller than 20 characters
    nor larger than 2000
    """
    assert descriptionCheck(
        'description small') is False
    assert descriptionCheck(
        'description is bigger than 20') is True


def test_r4_4_create_Listing():
    """
    Testing R4-4: Title size cannot be larger than description
    """
    assert title_description_Check(
        'aaaaaaaaaaaaaaaaaaaaaaaaaa' +
        'aaaaaaaaaaaaaaaaaaaaaaaaaa',
        'description is normal 20') is False
    assert title_description_Check(
        'aaaaaaaaaaaa',
        'description is normal 20') is True


def test_r4_5_create_Listing():
    """
    Testing R4-6: Price is too small or large
    """
    assert price_Check(9) is False
    assert price_Check(10001) is False
    assert price_Check(11) is True


def test_r4_7_create_Listing():
    """
    Testing R4-7-a: Owner email exists and not blank
    """
    user_registration('test1@test.com', 'u21', 'TestR2#1')
    
    assert user_registration('test1@test.com', 'u21', 'TestR2#1') is False
    assert user_registration('test2@test.com', 'u21', 'TestR2#1') is True


def test_r4_8_create_Listing():
    """
    Testing R4-8: if current title already exists
    """
    createListing(
        'aaaaaaaaaaaaaa',
        'description is normal 20',
        11, 'test1@test.com', '1')
    assert createListing(
        'aaaaaaaaaaaaaa',
        'description is normal 20',
        11, 'test1@test.com', '1') is False
    assert createListing(
        'bbbbbbbbbbb',
        'description is normal 20',
        11, 'test2@test.com', '2') is True