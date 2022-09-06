from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

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
