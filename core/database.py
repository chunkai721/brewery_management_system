from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class DatabaseConnection:
    def connect(self):
        pass

    def close(self):
        pass

    def add_user(self, user):
        # 新增用戶到資料庫
        pass

    def get_user(self, username):
        # 從資料庫獲取用戶資訊
        pass
