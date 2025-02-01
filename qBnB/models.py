from qBnB import app
from flask_sqlalchemy import SQLAlchemy

# flask SQLAlchemy reference documentation
# https://flask-sqlalchemy.palletsprojects.com/en/latest/quickstart/#check-the-sqlalchemy-documentation

# foreign keys documentation
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

# query documentation
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/

# create the app
# app = Flask(__name__)

# configure the SQLite database, relative to the app instance folder
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

# create the extension
db = SQLAlchemy(app)


# create transaction table
class Booking(db.Model):
    __tablename__ = 'booking'

    id = db.Column(db.String(36), primary_key=True)
    user_id = db.Column(db.String(36), unique=True, nullable=False)
    listing_id = db.Column(db.String(36), unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=True)

    # display class object as string
    def __repr__(self):
        return '<Bookings %r>' % self.id


# create transaction table
class User(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.String(36), primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    billing_address = db.Column(db.String, unique=False, nullable=False)
    postal_code = db.Column(db.String, unique=False, nullable=True)
    balance = db.Column(db.Integer, unique=False, nullable=False)

    # display class object as string
    def __repr__(self):
        return '<User %r>' % self.user_id


# create product review table
class Review(db.Model):
    __tablename__ = 'review'

    id = db.Column(db.String(8), primary_key=True)
    user_id = db.Column(db.String(36), unique=True, nullable=False)
    listing_id = db.Column(db.String(8), unique=True, nullable=False)
    review_test = db.Column(db.String(1000), nullable=False)
    date = db.Column(db.Date, nullable=False)

    # display class object as string
    def __repr__(self):
        return '<Review %r>' % self.id


# create listings table
class Listing(db.Model):
    __tablename__ = 'listing'

    id = db.Column(db.String(36), nullable=False)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(2000))
    price = db.Column(db.Integer, nullable=False)
    last_modified_date = db.Column(db.Date, nullable=False)
    owner_id = db.Column(db.String(36), primary_key=True, nullable=False)

    # display class object as string
    def __repr__(self):
        return '<Listing %r>' % self.id


# create all tables
db.create_all()


