#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Zoo app</h1>'

# Routes to display information
@app.route('/')
def index():
    animals = Animal.query.all()
    zookeepers = Zookeeper.query.all()
    enclosures = Enclosure.query.all()
    return render_template('index.html', animals=animals, zookeepers=zookeepers, enclosures=enclosures)

@app.route('/animal/<int:id>')
def animal_by_id(id):
    animal = Animal.query.get_or_404(id)
    return render_template('animal_by_id.html', animal=animal)

@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.get_or_404(id)
    return render_template('zookeeper_by_id.html', zookeeper=zookeeper)

@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    enclosure = Enclosure.query.get_or_404(id)
    return render_template('enclosure_by_id.html', enclosure=enclosure)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
