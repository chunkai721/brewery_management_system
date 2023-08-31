from core.database import db
from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session
from membership.management import MembershipManagement
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__, template_folder='ui/templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'site.db')
app.config['SECRET_KEY'] = 'your_secret_key'
app.secret_key = 'your_secret_key_here'
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = MembershipManagement().login_user(email, password)
        if user:
            session['username'] = user.username  # 現在 user 是一個用戶對象
            flash('Logged in successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid email or password.', 'danger')
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        MembershipManagement().register_user(username, password, email)
        flash('Registered successfully!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove the username from session
    flash('Logged out successfully!', 'success')
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
