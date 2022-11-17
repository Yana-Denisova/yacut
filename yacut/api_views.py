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