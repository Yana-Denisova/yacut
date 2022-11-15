from flask import render_template, flash

from . import app, db
from .forms import UrlCutForm
from .models import URL_map


#def get_unique_short_id():

@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = UrlCutForm()
    if form.validate_on_submit():
        original_link = form.original_link.data
        custom_id = form.custom_id.data
        if URL_map.query.filter_by(custom_id=custom_id).first():
            flash('Такое вариант короткой ссылки уже существует!')
            return render_template('index.html', form=form)
        new_url = URL_map(
            original = original_link,
            short = custom_id
        )
    return render_template('index.html', form=form)