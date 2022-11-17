from flask import jsonify, request
from . import app, db
from .models import URL_map


@app.route('/api/id/', methods=['POST'])  
def add_url():
    data = request.get_json()
    url = URL_map()
    url.from_dict(data)
    db.session.add(url)
    db.session.commit()
    return jsonify(url.to_dict()), 201

@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_url(short_id):
    link = URL_map.query.filter_by(short=short_id).first()
    return jsonify({'url': link.original}), 200
