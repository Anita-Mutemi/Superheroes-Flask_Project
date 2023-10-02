from app import db
from models import Hero, Power, HeroPower

print ("🦸‍♀️ Seeding powers...")
powers = [
  Power(name="super strength", description="gives the wielder super-human strengths"),
  Power(name="flight", description="gives the wielder the ability to fly through the skies at supersonic speed"),
  Power(name="super human senses", description="allows the wielder to use her senses at a super-human level"),
  Power(name="elasticity", description="can stretch the human body to extreme lengths")
]
db.session.add_all(powers)

print ("🦸‍♀️ Seeding heroes...")
heroes= [
  Hero(name="Kamala Khan", super_name="Ms. Marvel"),
  Hero(name="Doreen Green", super_name="Squirrel Girl"),
  Hero(name="Gwen Stacy", super_name="Spider-Gwen"),
  Hero(name="Janet Van Dyne", super_name="The Wasp"),
  Hero(name="Wanda Maximoff", super_name="Scarlet Witch"),
  Hero(name="Carol Danvers", super_name="Captain Marvel"),
  Hero(name="Jean Grey", super_name="Dark Phoenix"),
  Hero(name="Ororo Munroe", super_name="Storm"),
  Hero(name="Kitty Pryde", super_name="Shadowcat"),
  Hero(name="Elektra Natchios", super_name="Elektra")
]
db.session.add_all(heroes)

print("🦸‍♀️ Adding powers to heroes...")
strengths = ["Strong", "Weak", "Average"]

Hero.all.each do |hero|
  rand(1..3).times do
    # get a random power
    power = Power.find(Power.pluck(:id).sample)

    HeroPower.create!(hero_id: hero.id, power_id: power.id, strength: strengths.sample)
  end
end

puts "🦸‍♀️ Done seeding!"
