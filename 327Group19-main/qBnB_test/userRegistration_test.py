from qBnB.backend import user_registration, user_login
from qBnB.backend import usernameCheck, emailCheck, passwordCheck


def test_r1_1_user_registration():
    """
    Testing R1-1: Email cannot be empty. password cannot be empty.
    """
    assert emailCheck('') is False


def test_r1_2_user_registration():
    """
    Testing R1-2: A user is uniquely
    identified by his/her user id -
    automatically generated.
    """
    user = user_registration('test2@test.com', 'u02', 'TestR1#2')
    assert len(user.user_id) == 36


def test_r1_3_user_registration():
    """
    Testing R1-3: The email has to follow addr-spec defined in RFC 5322.
    """
    assert emailCheck('test3test.com') is False
    assert emailCheck('test3@test,com') is False
    assert emailCheck('test3@test.com') is True


def test_r1_4_user_registration():
    """
    Testing R1-4: Password has to meet
    the required complexity: minimum length 6,
    at least one upper case,
    at least one lower case, and at
    least one special character.
    """
    assert passwordCheck('Te1#') is False
    assert passwordCheck('testr1#4') is False
    assert passwordCheck('TESTR1#4') is False
    assert passwordCheck('TestR144') is False
    assert passwordCheck('TestR1#4') is True


def test_r1_5_user_registration():
    """
    Testing R1-5: User name
    has to be non-empty, alphanumeric-only,
    and space allowed only if it is not as the
    prefix or suffix.
    """
    assert usernameCheck('u05#') is False
    assert usernameCheck('u05 ') is False
    assert usernameCheck(' u05') is False
    assert usernameCheck('user 05') is True


def test_r1_6_user_registration():
    """
    Testing R1-6: User name has to be longer
    than 2 characters and less than 20
    characters.
    """
    assert usernameCheck('u') is False
    assert usernameCheck('userUserUSERuSeRUsEr6666') is False


def test_r1_7_user_registration():
    """
    Testing R1-7: If the email has been used, the operation failed.
    """
    x = user_registration('test7@test.com', 'u07', 'TestR1#7')
    assert x.username == 'u07'
    y = user_registration('test07@test.com', 'u70', 'TestR1#7')
    assert y.username == 'u70'
    assert user_registration('test7@test.com', 'u77', 'TestR1#7') is False


def test_r1_8_user_registration():
    """
    Testing R1-8: Shipping address is empty at the time of registration.
    """
    user = user_registration('test8@test.com', 'u08', 'TestR1#8')
    assert user.billing_address == ''


def test_r1_9_user_registration():
    """
    Testing R1-9: Postal code is empty at the time of registration.
    """
    user = user_registration('test9@test.com', 'u09', 'TestR1#9')
    assert user.postal_code == ''


def test_r1_10_user_registration():
    """
    Testing R1-10: Balance should be
    initialized as 100 at the time of
    registration. (free $100 dollar signup bonus).
    """
    user = user_registration('test10@test.com', 'u10', 'TestR1#10')
    assert user.balance == 100


def test_r2_1_user_login():
    """
    Testing R2-1: A user can
     log in using her/his email
     address and the password.
    """
    x = user_registration('test21@test.com', 'u21', 'TestR2#1')
    assert x.username == 'u21'
    y = user_login('test21@test.com', 'TestR2#1')
    assert len(y.user_id) == 36


def test_r2_2_user_login():
    """
    R2-2: The login function should check if the supplied inputs meet the
    same email/password requirements as above, before checking the database.
    """
    user_registration('test22@test.com', 'u22', 'TestR2#2')

    assert user_login('test22@test,com', 'TestR2#2') is False
    assert user_login('test22@test.com', 'testr2#2') is False
    assert user_login('test22@test.com', 'TESTR2#2') is False
    assert user_login('test22@test.com', 'TestR22') is False

    assert user_login('test22@test.com', 'TestR2$2') is False

    user = user_login('test22@test.com', 'TestR2#2')
    assert len(user.user_id) == 36
