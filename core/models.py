from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

class Inventory:
    pass

class ProductionPlan:
    pass

class Sales:
    pass

class Customer:
    pass

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = self.encrypt_password(password)
        self.email = email
        self.date_joined = datetime.now()
        self.last_login = None
        self.profile_picture = None

    def encrypt_password(self, password):
        # 使用 bcrypt 或其他方法加密密碼
        pass

    def check_password(self, password):
        # 檢查密碼是否正確
        pass


