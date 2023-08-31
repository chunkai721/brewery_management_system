from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # 使用 SQLite 作為示範，您可以選擇其他資料庫
db = SQLAlchemy(app)

@app.route('/')
def home():
    return "Hello, Brewery Management System!"

if __name__ == "__main__":
    app.run(debug=True)
