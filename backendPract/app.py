from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector
from config import DB_CONFIG



app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

try:
    conn = mysql.connector.connect(**DB_CONFIG)
    print("✅ Connected to MySQL Workbench Database Successfully!")
    conn.close()
except mysql.connector.Error as err:
    print(f"❌ Error: {err}")


def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)



@app.route('/waste', methods=['GET'])
def get_waste_items():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM waste_items")
    data = cursor.fetchall()
    cursor.close()
    db.close()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
