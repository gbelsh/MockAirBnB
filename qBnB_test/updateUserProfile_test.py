from qBnB.backend import postalCodeCheck, updateProfile
from qBnB.backend import usernameCheck


def test_r3_1_update_user_profile():
    """
    Testing R3_1: A user is only able to update his/her 
    user name, user email, billing address, and postal code.
    """   
    assert updateProfile('12345678', 
                         'user#1 ', 
                         'test@test.com', 
                         '101 union St', 
                         'K7L2J8') is False
    assert updateProfile('12345678', 
                         'user 02', 
                         'test@test.com',
                         '101 Union St', 
                         'F7L2J8') is False
    assert updateProfile('12345678', 
                         'user 03', 
                         'test2@test2.com', 
                         '102 Union St', 
                         'K7L2J9') is True


def test_r3_2_update_user_profile():
    """
    Testing R3_2: postal code should be non-empty, alphanumeric-only, 
    and no special characters such as !.
    """
    assert postalCodeCheck('') is False
    assert postalCodeCheck('K7!2J8') is False
    assert postalCodeCheck('&8H7K$') is False
    assert postalCodeCheck('K7L2J8') is True


def test_r3_3_update_user_profile():
    """
    Testing R3_3: Postal code has to be a valid Canadian postal code.
    """
    assert postalCodeCheck('O7L2J8') is False
    assert postalCodeCheck('F7L2J8') is False
    assert postalCodeCheck('K7D2J8') is False
    assert postalCodeCheck('K7I2J8') is False
    assert postalCodeCheck('K7L2Q8') is False
    assert postalCodeCheck('K7L2U8') is False
    assert postalCodeCheck('ABCDEJ') is False
    assert postalCodeCheck('123456') is False
    assert postalCodeCheck('K1P0A9') is True


def test_r3_4_update_user_profile():
    """
    Testing R3_4: User name follows the requirements above.
    """
    assert usernameCheck('') is False
    assert usernameCheck('user#2') is False
    assert usernameCheck(' user3') is False
    assert usernameCheck('user4 ') is False
    assert usernameCheck('user 5') is True