from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NamerForm(FlaskForm):
    name = StringField("Your name", validators=[DataRequired()])
    submit = SubmitField("Submit")


class Userform(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("E-mail", validators=[DataRequired()])
    submit = SubmitField("Submit")