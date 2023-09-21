#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/bakeries', methods=['GET'])
def get_bakeries():
    bakeries = Bakery.query.all()
    bakery_list = [{'id': bakery.id, 'name': bakery.name, 'created_at': bakery.created_at} for bakery in bakeries]
    return jsonify(bakery_list)

@app.route('/bakeries/<int:id>', methods=['GET'])
def get_bakery_by_id(id):
    bakery = Bakery.query.get(id)
    if bakery is None:
        return jsonify({'error': 'Bakery not found'}), 404
    return jsonify({'id': bakery.id, 'name': bakery.name, 'created_at': bakery.created_at})

# Implement similar routes and handlers for '/baked_goods' and '/baked_goods/most_expensive'

if __name__ == '__main__':
    app.run(debug=True)