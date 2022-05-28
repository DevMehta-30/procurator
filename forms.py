from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField,IntegerField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
import phonenumbers


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[Email(), DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Login')


class RegisterForm(FlaskForm):
    email_address = StringField(label='Email', validators=[Email(), DataRequired()])
    password = PasswordField(label='Password', validators=[Length(min=6), DataRequired()])
    confirm_password = PasswordField(label='Confirm Password', validators=[EqualTo('password'), DataRequired()])
    radio_btn = RadioField(label="radio button", choices=[("Manager", "Manager"), ("Employee", "Employee")], default="Manager", validate_choice=[DataRequired()])
    submit = SubmitField(label='Register')


class DonorDetailsForm(FlaskForm):
    name = StringField(label='Name:', validators=[Length(max=30), DataRequired()])
    work = StringField(label='Work Done', validators=[Length(max=50), DataRequired()])
    hours = IntegerField(label="No. of Hours", validators=[Length(max=24), DataRequired()])
    submit = SubmitField(label='submit')

    def validate_contact(self, field):
        if not len(field.data) == 10:
            raise ValidationError('Invalid phone number.')

        try:
            input_number = phonenumbers.parse(field.data, "IN")
            if not (phonenumbers.is_valid_number(input_number)):
                raise ValidationError('Invalid phone number.')
        except:
            input_number = phonenumbers.parse("+91" + field.data)
            if not (phonenumbers.is_valid_number(input_number)):
                raise ValidationError('Invalid phone number.')
