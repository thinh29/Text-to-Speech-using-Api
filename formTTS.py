from flask_wtf import FlaskForm
from wtforms import Form, StringField, TextAreaField, SelectField, SubmitField, FloatField
from wtforms.validators import DataRequired, Length
from gtts.lang import tts_langs


speaker_id = [(1, "Nữ miền nam"), (2, "Nữ miền bắc"), (3, "Nam miền nam"), (4,"Nam miền bắc")]
langs = tts_langs()
langs_s = []
for i in langs:
	langs_s.append( (i,langs[i]) )

class GtextToSpeech(FlaskForm):
    text = TextAreaField("Nhập nội dụng cần chuyển đổi . Tối đa 2000 kí tự .....")
    lang = SelectField('Language',choices=langs_s)
    submit = SubmitField('Bắt đầu chuyển đổi')

class ZtextToSpeech(FlaskForm):
    api = StringField("Nhập API")
    text = TextAreaField("Nhập nội dụng cần chuyển đổi . Tối đa 2000 kí tự .....")
    speaker_id = SelectField('Giọng đọc',choices=speaker_id)
    speed = FloatField("Tốc độ")
    submit = SubmitField('Bắt đầu chuyển đổi')
    