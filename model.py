from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String, unique=True,nullable=False)
    password = db.Column(db.String, nullable=False)
    firstname = db.Column(db.String, nullable=False)
    lastname = db.Column(db.String)
    email = db.Column(db.String, unique=True, nullable=False)
    door_no = db.Column(db.String, nullable=False)
    street_addr = db.Column(db.String, nullable=False)
    zipcode = db.Column(db.String, nullable=False)
    city= db.Column(db.String, nullable=False)
    state = db.Column(db.String, nullable=False)
    country = db.Column(db.String, nullable=False)
    phone_no = db.Column(db.String, nullable=False)
    created_date = db.Column(db.DateTime, nullable=False)

   

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'




class Product(db.Model):
    """A product."""

    __tablename__ = 'products'

    product_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    title = db.Column(db.String, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('product_category.category_id'))
    description = db.Column(db.String)
    s3_image_url = db.Column(db.String)
    s3_video_url = db.Column(db.String)
    condition = db.Column(db.String, nullable=False)
    available_from = db.Column(db.DateTime, nullable=False)
    available_to= db.Column(db.DateTime, nullable=False)
    price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String, nullable=False)
    isverified = db.Column(db.String, nullable=False)
    created_date = db.Column(db.DateTime, nullable=False)

    
    owner = db.relationship('User', backref='products')
    product_category = db.relationship('ProductCategory', backref='products')
   

    def __repr__(self):
        return f'<Product product_id={self.product_id} title={self.title}>'


class ProductCategory(db.Model):
    """A product category."""

    __tablename__ = 'product_category'

    category_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    category_name = db.Column(db.String, nullable=False)
    created_date = db.Column(db.DateTime, nullable=False)

    
    def __repr__(self):
        return f'<Product Category category_id={self.product_id} name={self.category_name}>'




class RentedProduct(db.Model):
    """A Rented Product."""

    __tablename__ = 'rented_products'

    rented_product_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'))
    owner_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    renter_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    rented_from = db.Column(db.DateTime, nullable=False)
    rented_to=  db.Column(db.DateTime, nullable=False)
    price = db.Column(db.Float, nullable=False)
    payment_id = db.Column(db.Integer ,nullable=False)
    created_date = db.Column(db.DateTime, nullable=False)

    owner = db.relationship('User', backref='rented_products',foreign_keys=[owner_id])
    renter = db.relationship('User', backref='renters',foreign_keys=[renter_id])
    product = db.relationship('Product', uselist=False, backref='rented_product')
   
   

    def __repr__(self):
        return f'<Rented Product rented_product_id={self.rented_product_id} product_id={self.product_id}>'


def connect_to_db(flask_app, db_uri='postgresql:///renteasi', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')



if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
