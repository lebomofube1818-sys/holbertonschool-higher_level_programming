#!/usr/bin/python3
from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    items_file = os.path.join(os.path.dirname(__file__), 'items.json')
    items_list = []

    try:
        with open(items_file, 'r') as f:
            data = json.load(f)
            items_list = data.get("items", [])
    except FileNotFoundError:
        print("items.json not found. Displaying empty list.")
    except json.JSONDecodeError:
        print("Error decoding JSON. Displaying empty list.")

    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
