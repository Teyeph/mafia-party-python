from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired


class HomeForm(FlaskForm):
    nickname = StringField('nickname', validators=[InputRequired()])
    room_code = StringField('join room')
    join_button = SubmitField('join')
    create_button = SubmitField('create room')
