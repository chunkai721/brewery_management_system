from core.database import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def verify_password(self, password):
        return check_password_hash(self.password, password)

    def encrypt_password(self, password):
        # 使用 bcrypt 或其他方法加密密碼
        pass

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Inventory:
    pass

class ProductionPlan:
    pass

class Sales:
    pass

class Customer:
    pass




