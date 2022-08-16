from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import length, EqualTo, Email, DataRequired, ValidationError
from market.models import User

class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user=User.query.filter_by(username=username_to_check.data).first()
        if (user):
            raise ValidationError(" Username already exists! Please try with a different username.")
    
    def validate_email(self,email_to_check):
        email=User.query.filter_by(email=email_to_check.data).first()
        if email:
            raise ValidationError("Account with this email address already exists! Please try with a different email address.")

    username = StringField(label='User Name', validators=[length(min=3,max=30), DataRequired()])
    email = StringField(label='Email Address', validators=[Email(), DataRequired()])
    password1 = PasswordField(label = "Password", validators=[length(min=6), DataRequired()])
    password2 = PasswordField(label = "Confirm Password", validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')

class LoginForm(FlaskForm):
    username = StringField(label="User Name : ", validators=[DataRequired()])
    password = PasswordField(label="Password : ", validators=[DataRequired()])
    submit = SubmitField(label='Sign In')

class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label="Purchase Item now!")

class SellItemForm(FlaskForm):
    submit = SubmitField(label="Sell Item now!")