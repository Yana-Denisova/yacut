from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, Regexp


class UrlCutForm(FlaskForm):
    original_link = URLField(
        'Добавьте ссылку для обработки',
        validators=[DataRequired(message='Обязательное поле'),
                    Length(1, 256)]
    )
    custom_id = StringField(
        'Придумайте свой вариант краткой ссылки', 
        validators=[Length(1, 16), Optional(),
        Regexp(regex=r'\w+')]
    )
    submit = SubmitField('Создать')
