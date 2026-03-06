#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv
import sqlite3
import os

app = Flask(__name__)

# --- Task 3 functions ---
def read_json(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception:
        return []

def read_csv(file_path):
    data = []
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                data.append(row)
        return data
    except Exception:
        return []

# --- New: SQLite reading function ---
def read_sqlite(db_path):
    data = []
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Products")
        rows = cursor.fetchall()
        for row in rows:
            data.append({
                "id": row["id"],
                "name": row["name"],
                "category": row["category"],
                "price": row["price"]
            })
        conn.close()
        return data
    except Exception:
        return []

@app.route('/products')
def products():
    source = request.args.get('source', '').lower()
    prod_id = request.args.get('id', None)

    json_file = os.path.join(os.path.dirname(__file__), 'products.json')
    csv_file = os.path.join(os.path.dirname(__file__), 'products.csv')
    db_file = os.path.join(os.path.dirname(__file__), 'products.db')

    error = None
    products_data = []

    if source == 'json':
        products_data = read_json(json_file)
    elif source == 'csv':
        products_data = read_csv(csv_file)
    elif source == 'sql':
        products_data = read_sqlite(db_file)
    else:
        error = "Wrong source"

    # Filter by id if provided
    if prod_id and not error:
        try:
            prod_id_int = int(prod_id)
            filtered = [p for p in products_data if p.get('id') == prod_id_int]
            if not filtered:
                error = "Product not found"
            else:
                products_data = filtered
        except ValueError:
            error = "Invalid id"

    return render_template('product_display.html', products=products_data, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
