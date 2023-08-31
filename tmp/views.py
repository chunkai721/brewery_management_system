from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from . import app, db
from .models import User, Inventory, Production, Sales, Keg
from .forms import UserForm, InventoryForm, ProductionForm, SalesForm, KegForm

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = UserForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        user = User(username=form.username.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful. Please login.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = UserForm()
    if form.validate_on_submit():
        user = User.query.get(form.username.data)
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Login successful.', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check username and password.', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))

@app.route('/inventory', methods=['GET', 'POST'])
@login_required
def inventory():
    form = InventoryForm()
    if form.validate_on_submit():
        item = Inventory(item_name=form.item_name.data, quantity=form.quantity.data, unit=form.unit.data)
        db.session.add(item)
        db.session.commit()
        flash('Item added to inventory.', 'success')
        return redirect(url_for('inventory'))
    items = Inventory.query.all()
    return render_template('inventory.html', form=form, items=items)

@app.route('/production', methods=['GET', 'POST'])
@login_required
def production():
    form = ProductionForm()
    if form.validate_on_submit():
        production = Production(product_name=form.product_name.data, quantity=form.quantity.data)
        db.session.add(production)
        db.session.commit()
        flash('Production added.', 'success')
        return redirect(url_for('production'))
    productions = Production.query.all()
    return render_template('production.html', form=form, productions=productions)

@app.route('/sales', methods=['GET', 'POST'])
@login_required
def sales():
    form = SalesForm()
    if form.validate_on_submit():
        sale = Sales(customer_name=form.customer_name.data, product_name=form.product_name.data, quantity=form.quantity.data)
        db.session.add(sale)
        db.session.commit()
        flash('Order added.', 'success')
        return redirect(url_for('sales'))
    sales = Sales.query.all()
    return render_template('sales.html', form=form, sales=sales)

@app.route('/keg', methods=['GET', 'POST'])
@login_required
def keg():
    form = KegForm()
    if form.validate_on_submit():
        keg = Keg.query.get(form.id.data)
        if keg:
            keg.location = form.location.data
            keg.status = form.status.data
            db.session.commit()
            flash('Keg updated.', 'success')
        else:
            flash('Keg not found.', 'danger')
        return redirect(url_for('keg'))
    kegs = Keg.query.all()
    return render_template('keg.html', form=form, kegs=kegs)
