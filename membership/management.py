# membership/management.py

from core.models import User
from core.database import db
from werkzeug.security import generate_password_hash

class MembershipManagement:

    def register_user(self, username, password, email):
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

    def login_user(self, email, password):
        user = User.query.filter_by(email=email).first()  # 假設 User 是您的數據庫模型
        if user and user.check_password(password):  # 假設 check_password 是一個驗證密碼的方法
            return user
        return None
