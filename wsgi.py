from flask import Flask, jsonify
from dice_roller_test.dice import Dice

app = Flask(__name__)

@app.route('/')
def home():
    dice = Dice()
    roll = dice.roll()
    return jsonify({'roll': roll})

@app.route('/hello')
def hello():
    return jsonify({'Hello': 'There'})
