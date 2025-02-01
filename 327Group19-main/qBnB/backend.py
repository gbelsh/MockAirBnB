from qBnB.models import db, Listing, User, Booking
from uuid import uuid4
from validate_email import validate_email
import re
import datetime as dt


def usernameCheck(username):
    # username = input("Enter a username")  # User enters username
    # check username
    # Regex used to make sure username follows:
    # within 2 to 20 char limit
    # alphanumeric only
    # one space that is not a suffix or prefix
    regexUsername = "^[a-zA-Z0-9]+[a-zA-Z0-9 ]?[a-zA-Z0-9]+$"
    if not username:  # Username was left empty
        return False  # "username was left empty"

    # Checks if username was outside the 2-20 char limit:
    if not (2 < len(username) < 20):
        return False  # "The length of the username is incorrect"

    # Checks if the username is within the regex:
    if re.match(regexUsername, username) is None:
        return False  # "Username not allowed within parameters"

    return True


def emailCheck(email):
    # Check email
    # regex expressions used to
    # check if email follows RCF 5322

    if not email:
        return False  # "email was left empty"

    if not validate_email(email):
        return False  # "Email does not follow RCF 5322"

    existed = User.query.filter_by(email=email).all()
    if len(existed) > 0:
        return False  # "this email has been used before"
    return True


def emailCheck_login(email):
    # Check email
    # regex expressions used to
    # This does not check for existed emails
    # check if email follows RCF 5322
    if not email:
        return False  # "email was left empty"

    if not validate_email(email):
        return False  # "Email does not follow RCF 5322"

    return True


def passwordCheck(password):
    # password = input("Enter a password")
    # Check password
    # Regex to make sure password follows:
    # min length 6
    # At least one upper case
    # At least one lower case
    # At least one special char
    regexPassword = '^(?=.*[a-z])(?=.*[A-Z])' \
                    '(?=.*\W)[A-Za-z\d\W]{6,}$'

    if not password:
        return False  # ("password was left empty")

    if re.match(regexPassword, password) is None:
        return False  # "Password does not adhere to specifications")

    return True


def user_login(email, password):
    """
    LOGIN CHECK
    """
    valids = User.query.filter_by(email=email, password=password).all()
    if not emailCheck_login(email) or not passwordCheck(password):
        return False  # email or password checks failed
    if len(valids) != 1:
        return False  # Login Failed
    # Login Successful
    return valids[0]


def user_registration(email, username, password):
    # Function to ask user to input registration data

    if emailCheck(email) and usernameCheck(username) \
            and passwordCheck(password):
        registerUser = User(
            user_id=str(uuid4()), email=email, username=username,
            password=password, billing_address='', postal_code='', balance=100)
        db.session.add(registerUser)
        db.session.commit()
        # return registerUser  # For Testing
        return True
    return False


# checks if postal code is both a valid Canadian postal code
# and non-empty, alphanumeric, with no special characters
def postalCodeCheck(postalCode):
    # regex expression for valid Canadian postal codes
    # currently only allows for upper case letters due
    # to validity reasons
    # Regex used to make sure postal code follows:
    # 6 characters long only
    # alphanumberic only
    # the 2nd, 4th, and 6th character is a digit 0 to 9
    # the 1st character can only be one of ABCEGHJKLMNPRSTVXY
    # the 3rd character can only be one of ABCEGHJKLMNPRSTVWXYZ
    # the 5th character can only be one of ABCEGHJKLMNPRSTVWXYZ
    regexPostalCode = "[ABCEGHJKLMNPRSTVXY]" \
                      "\d[ABCEGHJ-NPRSTV-Z][ ]?" \
                      "\d[ABCEGHJ-NPRSTV-Z]\d"

    # check if postalCode was left empty
    if not postalCode:
        return False

    # check if postal code is invalid in Canada
    if re.match(regexPostalCode, postalCode) is None:
        return False

    # postal code passes all checks and is valid
    return True


# allows user to update: username, email,
# billing address, and postal code
def updateProfile(userId, username, email, billingAddress, postalCode):
    """
    test_user = User(user_id='123345678',
                     email='test@test.com',
                     username='user 00',
                     password='87654321',
                     billing_address='101 union St',
                     postal_code='K7L2J8',
                     balance=100)
    db.session.add(test_user)
    """

    # check if username and postal code are valid
    # may need to check for email, billing address
    # in the future depending on other requirements
    if usernameCheck(username) and postalCodeCheck(postalCode) \
            and emailCheck_login(email):
        # find the user with the same user_id as the current user in the db
        updateUser = User.query.filter_by(user_id=userId).first()

        # update rows in the db for the corresponding user
        updateUser.username = username
        updateUser.email = email
        updateUser.billing_address = billingAddress
        updateUser.postal_code = postalCode
        db.session.commit()
        # changes were successful
        return True

    # username and/or postal code were invalid
    # changes were unsuccessful
    return False


def titleCheck(title):
    # Create regex, check title against regex, and find title size
    regexTitle = "^[a-zA-Z0-9]+(?:[a-zA-Z0-9]+)?$"

    # Find title in database
    curr_title = Listing.query.filter_by(title=title).all()
    size_of_title = len(title)
    # if title size outside limits
    if size_of_title > 80:
        return False
    # if title doesn't align with regex
    if re.match(regexTitle, title) is None:
        return False
    # Checks if title starts or ends with space
    elif title.startswith(' ') or title.endswith(' '):
        return False
    # Checks if current title exists in database
    elif curr_title:
        return False

    return True


def titleCheckUpdate(listID, title):
    # Create regex, check title against regex, and find title size
    regexTitle = "^[a-zA-Z0-9]+(?:[a-zA-Z0-9]+)?$"

    # Find title in database
    curr_title = Listing.query.filter(
        Listing.title == title, Listing.owner_id != listID).all()
    size_of_title = len(title)
    # if title size outside limits
    if size_of_title > 80:
        return False
    # if title doesn't align with regex
    if re.match(regexTitle, title) is None:
        return False
    # Checks if title starts or ends with space
    elif title.startswith(' ') or title.endswith(' '):
        return False
    # Checks if current title exists in database
    elif curr_title:
        return False

    return True


def descriptionCheck(description):
    # Find size of description
    size_of_description = len(description)

    # Checks if description is in bounds
    if 20 <= size_of_description <= 2000:
        return True
    return False


def title_description_Check(title, description):
    # Checks size of title against size of description
    titleSize = len(title)
    descriptionSize = len(description)

    if titleSize > descriptionSize:
        return False
    return True


def price_Check(price):
    # Checks if price is within bounds
    if 10 < price < 10000:
        return True
    return False


def last_modified_dateCheck(last_modified_date):
    # Checks if the modified date is within bounds
    if last_modified_date < dt.datetime(2021, 1, 2):
        return False
    elif last_modified_date > dt.datetime(2025, 1, 2):
        return False
    return True


# Create listing function
def createListing(
        title, description, price, email, uid):
    # Function to check if a listing meets requirements
    # to be created on qB&B

    last_modified_date = dt.datetime.now()
    if titleCheck(title) and \
            title_description_Check(title, description) \
            and descriptionCheck(description) and \
            price_Check(price) and \
            last_modified_dateCheck(last_modified_date) \
            and emailCheck_login(email):
        registerListing = Listing(
            id=uid, title=title, description=description,
            price=price, last_modified_date=last_modified_date,
            owner_id=str(uuid4())
        )
        db.session.add(registerListing)
        db.session.commit()
        return True
    return False


def priceCheck(oldPrice, price):
    # Ensuring old price is
    # less than new price
    if 10 < price < 10000:
        if oldPrice < price:
            return True
    return False


# Find owner id, owner email, and title in database
def updateListings(listID, title, description, price):
    upListing = Listing.query.filter_by(owner_id=listID).first()
    # checking if the information
    # being updated even exists first
    if titleCheckUpdate(listID, title) and \
            descriptionCheck(description) and \
            title_description_Check(title, description) and \
            priceCheck(upListing.price, price):
        upListing.title = title
        upListing.description = description
        upListing.price = price
        db.session.commit()
        # Update successful
        return True
    # Update Failed
    return False


def bookListing(listId, ownerId, year, month, day):
    listingUser = Listing.query.filter_by(owner_id=listId).one_or_none()
    bookingUser = User.query.filter_by(user_id=ownerId).one_or_none()

    year = int(year)
    month = int(month)
    day = int(day)

    # Check if user is trying to book their own listing
    if bookingUser.user_id == listingUser.id:
        # Failed booking
        return False

    # Check if user is trying to book a listing they cant afford
    if bookingUser.balance < listingUser.price:
        # Failed booking
        return False

    # Check if this booking has already been booked at this date
    dateBookings = Booking.query.filter_by(listing_id=listId).all()
    for dateBooking in dateBookings:
        if dateBooking.date == dt.datetime(year, month, day):
            # Failed booking
            return False

    # Add the booking info to the db
    registerBooking = Booking(id=str(uuid4()),
                              user_id=ownerId, listing_id=listId,
                              price=listingUser.price,
                              date=dt.datetime(year, month, day))
    bookingUser.balance = bookingUser.balance - listingUser.price

    db.session.add(registerBooking)
    db.session.commit()

    # Successful booking
    return True
