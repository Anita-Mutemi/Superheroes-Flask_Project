import random  # Import the random module
from app import db, Hero, Power, HeroPower

print("🦸‍♀️ Seeding powers...")
powers = [
  { "name": "super strength", "description": "gives the wielder super-human strengths" },
  { "name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed" },
  { "name": "super human senses", "description": "allows the wielder to use her senses at a super-human level" },
  { "name": "elasticity", "description": "can stretch the human body to extreme lengths" }
]

for power_data in powers:
    power = Power(**power_data)
    db.session.add(power)

print("🦸‍♀️ Seeding heroes...")
heroes = [
  { "name": "Kamala Khan", "super_name": "Ms. Marvel" },
  { "name": "Doreen Green", "super_name": "Squirrel Girl" },
  { "name": "Gwen Stacy", "super_name": "Spider-Gwen" },
  { "name": "Janet Van Dyne", "super_name": "The Wasp" },
  { "name": "Wanda Maximoff", "super_name": "Scarlet Witch" },
  { "name": "Carol Danvers", "super_name": "Captain Marvel" },
  { "name": "Jean Grey", "super_name": "Dark Phoenix" },
  { "name": "Ororo Munroe", "super_name": "Storm" },
  { "name": "Kitty Pryde", "super_name": "Shadowcat" },
  { "name": "Elektra Natchios", "super_name": "Elektra" }
]

for hero_data in heroes:
    hero = Hero(**hero_data)
    db.session.add(hero)

print("🦸‍♀️ Adding powers to heroes...")
strengths = ["Strong", "Weak", "Average"]

for hero in Hero.query.all():
    for _ in range(1, 4):  # Randomly assign 1 to 3 powers to each hero
        power = Power.query.get(random.randint(1, len(powers)))  # Fix here
        strength = random.choice(strengths)  # Fix here
        hero_power = HeroPower(hero=hero, power=power, strength=strength)
        db.session.add(hero_power)

print("🦸‍♀️ Done seeding!")
db.session.commit()
