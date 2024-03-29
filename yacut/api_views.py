import re

from http import HTTPStatus
from flask import jsonify, request

from . import app, db
from .models import URL_map
from .errors import InvalidAPIUsage
from .views import get_unique_short_id


@app.route('/api/id/', methods=['POST'])
def add_url():
    data = request.get_json()
    if data is None:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    elif 'url' not in data:
        raise InvalidAPIUsage('\"url\" является обязательным полем!')
    elif 'custom_id' not in data or data['custom_id'] == '' or data['custom_id'] is None:
        data.update(custom_id=get_unique_short_id())
    elif not re.match(r'[a-zA-Z0-9]+$', data['custom_id']):
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
    elif len(data['custom_id']) > 16:
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
    elif URL_map.query.filter_by(short=data['custom_id']).first():
        raise InvalidAPIUsage(f'Имя "{data["custom_id"]}" уже занято.')
    url = URL_map()
    url.from_dict(data)
    db.session.add(url)
    db.session.commit()
    return jsonify(url.to_dict()), HTTPStatus.CREATED


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_url(short_id):
    link = URL_map.query.filter_by(short=short_id).first()
    if link is None:
        raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)
    return jsonify({'url': link.original}), HTTPStatus.OK
