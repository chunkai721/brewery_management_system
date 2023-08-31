## tests.py
import pytest
from flask import url_for
from brewery_management_system import create_app, db
from brewery_management_system.models import User, Inventory, Production, Sales, Keg

@pytest.fixture
def app():
    app = create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:'})
    with app.app_context():
        db.create_all()
        yield app
    db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200

def test_register(client):
    response = client.post('/register', data={'username': 'test', 'password': 'test', 'confirm_password': 'test'}, follow_redirects=True)
    assert response.status_code == 200
    user = User.query.get('test')
    assert user is not None

def test_login(client):
    client.post('/register', data={'username': 'test', 'password': 'test', 'confirm_password': 'test'}, follow_redirects=True)
    response = client.post('/login', data={'username': 'test', 'password': 'test'}, follow_redirects=True)
    assert response.status_code == 200

def test_inventory(client):
    client.post('/register', data={'username': 'test', 'password': 'test', 'confirm_password': 'test'}, follow_redirects=True)
    client.post('/login', data={'username': 'test', 'password': 'test'}, follow_redirects=True)
    response = client.post('/inventory', data={'item_name': 'test', 'quantity': 10, 'unit': 'kg'}, follow_redirects=True)
    assert response.status_code == 200
    item = Inventory.query.filter_by(item_name='test').first()
    assert item is not None

def test_production(client):
    client.post('/register', data={'username': 'test', 'password': 'test', 'confirm_password': 'test'}, follow_redirects=True)
    client.post('/login', data={'username': 'test', 'password': 'test'}, follow_redirects=True)
    response = client.post('/production', data={'product_name': 'test', 'quantity': 10}, follow_redirects=True)
    assert response.status_code == 200
    production = Production.query.filter_by(product_name='test').first()
    assert production is not None

def test_sales(client):
    client.post('/register', data={'username': 'test', 'password': 'test', 'confirm_password': 'test'}, follow_redirects=True)
    client.post('/login', data={'username': 'test', 'password': 'test'}, follow_redirects=True)
    response = client.post('/sales', data={'customer_name': 'test', 'product_name': 'test', 'quantity': 10}, follow_redirects=True)
    assert response.status_code == 200
    sale = Sales.query.filter_by(customer_name='test').first()
    assert sale is not None

def test_keg(client):
    client.post('/register', data={'username': 'test', 'password': 'test', 'confirm_password': 'test'}, follow_redirects=True)
    client.post('/login', data={'username': 'test', 'password': 'test'}, follow_redirects=True)
    keg = Keg(id=1, location='test', status='test')
    db.session.add(keg)
    db.session.commit()
    response = client.post('/keg', data={'id': 1, 'location': 'updated', 'status': 'updated'}, follow_redirects=True)
    assert response.status_code == 200
    keg = Keg.query.get(1)
    assert keg.location == 'updated'
    assert keg.status == 'updated'
