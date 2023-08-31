from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class User(UserMixin, db.Model):
    """User model."""
    __tablename__ = "users"

    username = db.Column(db.String(64), unique=True, nullable=False, primary_key=True)
    password = db.Column(db.String(128), nullable=False)
    is_authenticated = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=False)
    is_anonymous = db.Column(db.Boolean, default=False)

    def get_id(self):
        return self.username

class Inventory(db.Model):
    """Inventory model."""
    __tablename__ = "inventory"

    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(64), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    unit = db.Column(db.String(64), nullable=False)

class Production(db.Model):
    """Production model."""
    __tablename__ = "production"

    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(64), nullable=False)
    production_date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    quantity = db.Column(db.Integer, nullable=False)

class Sales(db.Model):
    """Sales model."""
    __tablename__ = "sales"

    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(64), nullable=False)
    product_name = db.Column(db.String(64), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    order_date = db.Column(db.Date, nullable=False, default=datetime.utcnow)

class Keg(db.Model):
    """Keg model."""
    __tablename__ = "kegs"

    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(64), nullable=False)
    status = db.Column(db.String(64), nullable=False)
