from flask_sqlalchemy import SQLAlchemy

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

class HeroPower(db.Model):
  __tablename__ = 'hero_power'
  id = db.Column(db.Integer, primary_key=True)
  strength = db.Column(db.Integer, nullable=False)

  hero_id = db.Column(db.Integer, db.ForeignKey('hero.id'))
  power_id = db.Column(db.Integer, db.ForeignKey('power.id'))

  hero = db.relationship('Hero', back_populates='powers')
  power = db.relationship('Power', back_populates='heroes')