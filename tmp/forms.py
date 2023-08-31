## forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo

class UserForm(FlaskForm):
    """Form for user registration and login."""
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=64)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Submit')

class InventoryForm(FlaskForm):
    """Form for adding items to the inventory."""
    item_name = StringField('Item Name', validators=[DataRequired(), Length(max=64)])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    unit = StringField('Unit', validators=[DataRequired(), Length(max=64)])
    submit = SubmitField('Submit')

class ProductionForm(FlaskForm):
    """Form for adding a new production."""
    product_name = StringField('Product Name', validators=[DataRequired(), Length(max=64)])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    submit = SubmitField('Submit')

class SalesForm(FlaskForm):
    """Form for adding a new order."""
    customer_name = StringField('Customer Name', validators=[DataRequired(), Length(max=64)])
    product_name = StringField('Product Name', validators=[DataRequired(), Length(max=64)])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    submit = SubmitField('Submit')

class KegForm(FlaskForm):
    """Form for updating a keg's location or status."""
    id = IntegerField('Keg ID', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired(), Length(max=64)])
    status = StringField('Status', validators=[DataRequired(), Length(max=64)])
    submit = SubmitField('Submit')
