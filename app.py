from flask import Flask, request, jsonify
from database import init_db, get_db_connection
import json

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "service": "ingestion-service"}), 200

@app.route('/api/v1/telemetry', methods=['POST'])
def ingest_data():
    data = request.json
    if not data:
        return jsonify({"error": "Payload is missing"}), 400
    
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Database connection failed"}), 500
    
    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO telemetry_data (payload) VALUES (%s)",
            (json.dumps(data),)
        )
        conn.commit()
        cursor.close()
        conn.close()
        
        return jsonify({"status": "success", "message": "Data ingested successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)