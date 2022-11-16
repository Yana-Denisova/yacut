import random
import string

from flask import render_template, flash, redirect, url_for, abort

from . import app, db
from .forms import UrlCutForm
from .models import URL_map


def get_unique_short_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = UrlCutForm()
    if form.validate_on_submit():
        original_url = form.original_link.data
        custom_url = form.custom_id.data
        if not custom_url or custom_url == '' or custom_url is None:
            custom_url = get_unique_short_id()
        if URL_map.query.filter_by(short=form.custom_id.data).first():
            flash('Такой вариант короткой ссылки уже существует!', 'fail')
        else:
            new_url = URL_map(
            original = original_url,
            short = custom_url
            )
            db.session.add(new_url)
            db.session.commit()
            flash(url_for('redirect_view', id = custom_url, _external=True), 'short_url')
            abort(500)
    return render_template('index.html', form=form)

@app.route('/<string:id>')
def redirect_view(id):
    link = URL_map.query.filter_by(short=id).first()
    return redirect(link.original)
