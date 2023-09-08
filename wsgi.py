from flask import Flask, jsonify
from dice_roller_test.dice import Dice

app = Flask(__name__)

@app.route('/')
def home():
    dice = Dice()
    return jsonify({'roll': dice.roll()})
