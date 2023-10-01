from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Hero(db.Model):
  __tablename__ = 'hero'  
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), nullable=False)
  secret_name = db.Column(db.String(80), nullable=False)
  age = db.Column(db.Integer)

  powers = db.relationship('HeroPower', back_populates='hero')

class Power(db.Model):
  __tablename__ = 'power'
  id = db.Column(db.Integer, primary_key=True)
  description = db.Column(db.String(255), nullable=False)
   
  heroes = db.relationship('HeroPower', back_populates='power')

  @validates('description')
  def validate_description(self, key, description):
    if not description:
      raise AssertionError(f'No {key} description provided')

    if len(description) < 2 or len(description) > 80:  
      raise AssertionError(f'{key} must be between 2 and 80 characters')

    return description

class HeroPower(db.Model):
  __tablename__ = 'hero_power'
  id = db.Column(db.Integer, primary_key=True)
  strength = db.Column(db.Integer, nullable=False)

  hero_id = db.Column(db.Integer, db.ForeignKey('hero.id'))
  power_id = db.Column(db.Integer, db.ForeignKey('power.id'))

  hero = db.relationship('Hero', back_populates='powers')
  power = db.relationship('Power', back_populates='heroes')

  @validates('strength')
  def validate_strength(self, key, strength):
    if strength < 0 or strength > 10:
      raise AssertionError(f'{key} must be between 0 and 10')
      
    return strength
  