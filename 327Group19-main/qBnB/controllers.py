from flask import render_template, request, session, redirect
from qBnB.models import Listing, User, Booking
from qBnB import app
from qBnB.backend import (user_login, user_registration,
                          updateProfile, usernameCheck,
                          emailCheck_login, postalCodeCheck,
                          createListing, updateListings,
                          passwordCheck, emailCheck,
                          titleCheck, descriptionCheck,
                          price_Check, priceCheck,
                          title_description_Check,
                          bookListing, titleCheckUpdate)


def authenticate(inner_function):
    """
    :param inner_function: any python function that accepts a user object
    Wrap any python function and check the current session to see if
    the user has logged in. If login, it will call the inner_function
    with the logged in user object.
    To wrap a function, we can put a decoration on that function.
    Example:
    @authenticate
    def home_page(user):
        pass
    """

    def wrapped_inner(*args, **kwargs):
        # check did we store the key in the session
        if 'logged_in' in session:
            user_id = session['logged_in']
            try:
                user = User.query.filter_by(user_id=user_id).one_or_none()
                if user:
                    # if the user exists, call the inner_function
                    # with user as parameter
                    return inner_function(user, *args, **kwargs)

            except Exception as e:
                print(e)
                return redirect('/login')
        else:
            # else, redirect to the login page
            return redirect('/login')

    # Renaming the function name:
    wrapped_inner.__name__ = inner_function.__name__
    # return the wrapped version of the inner_function:
    return wrapped_inner


@app.route('/login', methods=['GET'])
def login_get():
    return render_template('login.html', message='Please login')


@app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    user = user_login(email, password)
    if user:
        session['logged_in'] = user.user_id
        """
        Session is an object that contains sharing information 
        between a user's browser and the end server. 
        Typically it is packed and stored in the browser cookies. 
        They will be past along between every request the browser made 
        to this services. Here we store the user object into the 
        session, so we can tell if the client has already login 
        in the following sessions.
        """
        # success! go back to the home page
        # code 303 is to force a 'GET' request
        return redirect('/', code=303)
    else:
        if emailCheck_login(email) is False:
            error_message = "Email input incorrect format"
        elif passwordCheck(password) is False:
            error_message = "Password input incorrect format"
        else:
            error_message = "Login Failed"

        return render_template('login.html', message=error_message)


@app.route('/', methods=['GET', 'POST'])
@authenticate
def home(user):
    # authentication is done in the wrapper function
    # see above.
    # by using @authenticate, we don't need to re-write
    # the login checking code all the time for other
    # front-end portals

    listings = Listing.query.filter(Listing.id == user.user_id).all()
    bookings = Listing.query.filter(Listing.id != user.user_id).all()
    booked = Booking.query.filter(Booking.user_id == user.user_id).all()

    return render_template('index.html', user=user, listings=listings,
                           bookings=bookings, booked=booked)


@app.route('/register', methods=['GET'])
def register_get():
    # templates are stored in the templates folder
    return render_template('register.html', message='')


@app.route('/register', methods=['POST'])
def register_post():
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')
    password2 = request.form.get('password2')
    error_message = None

    if password != password2:
        error_message = "The passwords do not match"
    else:
        # use backend api to register the user
        success = user_registration(email, username, password)
        if not success:
            if emailCheck(email) is False:
                error_message = "Email input failed."
            elif usernameCheck(username) is False:
                error_message = "Username input failed."
            elif passwordCheck(password) is False:
                error_message = "Password input failed."

    # if there is any error messages when registering new user
    # at the backend, go back to the register page.
    if error_message:
        return render_template('register.html', message=error_message)
    else:
        return redirect('/login')


@app.route('/updateUser', methods=['GET'])
@authenticate
def update_get(user):
    # stored in the webpages folder
    return render_template('/updateUser.html', user=user, message="")


@app.route('/updateUser', methods=['POST'])
@authenticate
def update_post(user):
    user_ID = user.user_id
    username = request.form.get('username')
    user_email = request.form.get('email')
    billing_address = request.form.get('billingAddress')
    postal_code = request.form.get('postalCode')
    error_message = None

    success = updateProfile(user_ID, username, user_email,
                            billing_address, postal_code)
    if not success:
        if usernameCheck(username) is False:
            error_message = 'Invalid Username'
        elif emailCheck(user_email) is False:
            error_message = 'Invalid Email'
        elif postalCodeCheck(postal_code) is False:
            error_message = 'Invalid Postal Code'

    if error_message:
        return render_template('updateUser.html',
                               user=user, message=error_message)
    else:
        return redirect('/')


@app.route('/listing', methods=['GET'])
@authenticate
def listing_get(user):
    # stored in createListing folder
    return render_template('listing.html', user=user, message='')


@app.route('/listing', methods=['POST'])
@authenticate
def listing_post(user):
    title = request.form.get('title')
    description = request.form.get('description')
    price = request.form.get('price')
    error_message = None

    try:
        price = float(price)
    except ValueError:
        return render_template('listing.html', user=user,
                               message="Please Insert a Number for the Price")

    success = createListing(title, description, price,
                            user.email, user.user_id)

    if not success:
        if titleCheck(title) is False:
            error_message = "Title input incorrect"
        elif descriptionCheck(description) is False:
            error_message = "Description input incorrect"
        elif title_description_Check(title, description) is False:
            error_message = "Description is smaller than the Title"
        elif price_Check(price) is False:
            error_message = "Price input incorrect"
        else:
            error_message = "Error in creating Listing"

    if error_message:
        return render_template('listing.html',
                               user=user, message=error_message)
    else:
        return redirect('/')


@app.route('/updateListing/<listingID>', methods=['GET'])
@authenticate
def updateListings_get(user, listingID):
    upListing = Listing.query.filter_by(id=user.user_id, owner_id=listingID)\
        .one_or_none()
    if upListing is None:
        return render_template('error.html',
                               message="Listing not in your Listings!")
    return render_template('updateListing.html', listing=upListing, message='')


@app.route('/updateListing/<listingID>', methods=['POST'])
@authenticate
def updateListing_post(user, listingID):
    title = request.form.get('title')
    description = request.form.get('description')
    price = request.form.get('price')
    error_message = None

    upListing = Listing.query.filter_by(id=user.user_id, owner_id=listingID) \
        .one_or_none()
    if upListing is None:
        return render_template('error.html',
                               message="Listing not in your Listings!")

    try:
        price = float(price)
    except ValueError:
        return render_template('listing.html', user=user,
                               message="Please Insert a Number for the Price")

    success = updateListings(listingID, title, description, price)
    if not success:
        if titleCheckUpdate(listingID, title) is False:
            error_message = "Title input incorrect"
        elif descriptionCheck(description) is False:
            error_message = "Description input incorrect"
        elif title_description_Check(title, description) is False:
            error_message = "Description is smaller than the Title"
        elif priceCheck(upListing.price, price) is False:
            error_message = "Price input is either incorrect or " \
                            "smaller than the old price"
        else:
            error_message = "Error in Updating Listing"

    if error_message:
        return render_template('updateListing.html',
                               user=user, listing=upListing,
                               message=error_message)
    else:
        return redirect('/')


@app.route('/booking/<listID>/<userID>', methods=['GET'])
@authenticate
def booking_get(user, listID, userID):
    # stored in createListing folder

    listing = Listing.query.filter_by(owner_id=listID) \
        .one_or_none()
    if listing is None:
        return render_template('error.html',
                               message="listing does not exist!")

    return render_template('booking.html',
                           user=user, listing=listing, message='')


@app.route('/booking/<listID>/<userID>', methods=['POST'])
@authenticate
def booking_post(user, listID, userID):
    year = request.form.get('year')
    month = request.form.get('month')
    day = request.form.get('day')
    error_message = None

    listing = Listing.query.filter_by(owner_id=listID) \
        .one_or_none()
    if listing is None:
        return render_template('error.html',
                               message="listing does not exist!")

    success = bookListing(listID, userID, year, month, day)
    if not success:
        error_message = "Error in creating booking"

    if error_message:
        return render_template('booking.html',
                               user=user, message=error_message)
    else:
        return redirect('/')


@app.route('/logout')
def logout():
    if 'logged_in' in session:
        session.pop('logged_in', None)
    return redirect('/')
