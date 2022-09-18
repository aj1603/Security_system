from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email

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

class GameForm(FlaskForm):
    game_name = StringField('Ady', validators=[DataRequired()])
    description = StringField('Tanyşdyryş', validators=[DataRequired()])
    game_price = StringField('Oýunyň bahasy', validators=[DataRequired()])
    game_sale = StringField('Arzanladyş(%)', validators=[DataRequired()])
    today_sale = StringField('Arzanladyş(%)', validators=[DataRequired()])
    compitation = StringField('Ýaryşlar', validators=[DataRequired()])
    submit = SubmitField('Oýuny goş')


class GameUpdateForm(FlaskForm):
    game_name = StringField('Ady', validators=[DataRequired()])
    description = StringField('Tanyşdyryş', validators=[DataRequired()])
    game_price = StringField('Oýunyň bahasy', validators=[DataRequired()])
    game_sale = StringField('Arzanladyş(%)', validators=[DataRequired()])
    today_sale = StringField('Arzanladyş(%)', validators=[DataRequired()])
    compitation = StringField('Ýaryşlar', validators=[DataRequired()])
    submit = SubmitField('Tazelemek')

class DisCountForm(FlaskForm):
    today_sale = StringField('Arzanladyş(%)', validators=[DataRequired()])
    submit = SubmitField('Tazelemek')

class BuyForm(FlaskForm):
    buy_something = StringField('Satyn alynan harydyň bahasy', validators=[DataRequired()])
    submit = SubmitField('Satyn al!')

class LoginForm(FlaskForm):
    phone = StringField('Telefon', validators=[DataRequired()])
    password = PasswordField('Gizlin belgi', validators=[DataRequired()])
    remember = BooleanField('Ýatda sakla')
    submit = SubmitField('Içeri gir')