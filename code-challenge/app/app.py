#!/usr/bin/env python3

from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from models import db, Hero, Power, HeroPower 

from models import db, Hero

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return ''

@app.route("/heroes")
def get_heroes():
  heroes = Hero.query.all()
  return jsonify([hero.to_dict() for hero in heroes]) 

@app.route("/heroes/<int:hero_id>")
def get_hero(hero_id):
   hero = Hero.query.get(hero_id)
   if hero:
      return jsonify(hero.to_dict())
   else:
      return jsonify({"error": "Hero not found"}), 404

@app.route("/powers")  
def get_powers():
   powers = Power.query.all()
   return jsonify([power.to_dict() for power in powers]) 
   
@app.route("/powers/<int:power_id>")
def get_power(power_id):
   power = Power.query.get(power_id)
   if power:
    return jsonify(power.to_dict())
   else:
      return jsonify({"error": "Power not found"}), 404
   
@app.route("/powers/<int:power_id>", methods=['PATCH'])
def update_power(power_id):
   data = request.get_json()
   power = Power.query.get(power_id)
   if power:
    power.description = data['description']
    db.session.commit()
    return jsonify(power.to_dict())
   else:
    return jsonify({"error": "Power not found"}), 404
   
@app.route("/hero_powers", methods=['POST'])  
def create_hero_power():
   data = request.get_json()
   hero_power = HeroPower(
    hero_id=data['hero_id'], 
    power_id=data['power_id'],
    strength=data['strength']
    )
   db.session.add(hero_power)
   db.session.commit()
   return jsonify(hero_power.to_dict()), 201

if __name__ == '__main__':
    app.run(port=5555)
