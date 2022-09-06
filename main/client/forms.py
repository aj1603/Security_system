from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class ClientForm(FlaskForm):
    name = StringField('Ady', validators=[DataRequired()])
    surname = StringField('Familiýasy', validators=[DataRequired()])
    username = StringField('Ulanyjy ady', validators=[DataRequired()])
    password = StringField('Gizlin sözi', validators=[DataRequired()])
    phone_number = StringField('Telefone belgisi', validators=[DataRequired()])
    secret_key = StringField('Gizlin sözi', validators=[DataRequired()])
    play_time = StringField('Oýun oýnamaly wagty', validators=[DataRequired()])
    play_price = StringField('Oýnuň bahasy', validators=[DataRequired()])
    play_sale = StringField('Oýuna arzanlaşyk', validators=[DataRequired()])
    full_play_time = StringField('Köp wagtlyk bolsa', validators=[DataRequired()])
    submit = SubmitField('Oýunçy goş')


class ClientUpdateForm(FlaskForm):
    name = StringField('Ady', validators=[DataRequired()])
    surname = StringField('Familiýasy', validators=[DataRequired()])
    username = StringField('Ulanyjy ady', validators=[DataRequired()])
    password = StringField('Gizlin sözi', validators=[DataRequired()])
    phone_number = StringField('Telefone belgisi', validators=[DataRequired()])
    secret_key = StringField('Gizlin sözi', validators=[DataRequired()])
    play_time = StringField('Oýun oýnamaly wagty', validators=[DataRequired()])
    play_price = StringField('Oýnuň bahasy', validators=[DataRequired()])
    play_sale = StringField('Oýuna arzanlaşyk', validators=[DataRequired()])
    full_play_time = StringField('Köp wagtlyk bolsa', validators=[DataRequired()])
    submit = SubmitField('Oýunçy goş')