import re

from flask import jsonify, request

from . import app, db
from .models import URL_map
from .errors import InvalidAPIUsage
from .views import get_unique_short_id


@app.route('/api/id/', methods=['POST'])  
def add_url():
    data = request.get_json()
    if data is None:
        raise InvalidAPIUsage('Отсутствует тело запроса', 400)
    elif not data['url']:
        raise InvalidAPIUsage('"url" является обязательным полем!', 400)
    elif 'custom_id' not in data or data['custom_id'] == '' or len(data['custom_id']) > 16:
        data.update(custom_id=get_unique_short_id())
    elif not re.search(r'[a-zA-Z0-9]+', data['custom_id']):
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки', 400)
    url = URL_map()
    url.from_dict(data)
    db.session.add(url)
    db.session.commit()
    return jsonify(url.to_dict()), 201

@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_url(short_id):
    link = URL_map.query.filter_by(short=short_id).first()
    if link is None:
        raise InvalidAPIUsage('Указанный id не найден', 404)
    return jsonify({'url': link.original}), 200
