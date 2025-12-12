from flask import Flask, jsonify
import sqlite3

try:
    from flask_cors import CORS
    USE_CORS = True
except ImportError:
    CORS = None
    USE_CORS = False

DB_NAME = "landmarks.db"

app = Flask(__name__)

if USE_CORS and CORS is not None:
    CORS(app)


def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def row_to_landmark(row: sqlite3.Row) -> dict:
    return {
        "id": row["id"],
        "name": row["name"],
        "category": row["category"],
        "city": row["city"],
        "state": row["state"],
        "isFeatured": bool(row["isFeatured"]),
        "isFavorite": bool(row["isFavorite"]),
        "park": row["park"],
        "coordinates": {
            "latitude": row["latitude"],
            "longitude": row["longitude"],
        },
        "description": row["description"],
        "imageName": row["imageName"],
    }


@app.route("/landmarks", methods=["GET"])
def get_landmarks():
    conn = get_db_connection()
    rows = conn.execute("SELECT * FROM landmarks").fetchall()
    conn.close()

    landmarks = [row_to_landmark(row) for row in rows]
    return jsonify(landmarks)


@app.route("/landmarks/<int:landmark_id>", methods=["GET"])
def get_landmark(landmark_id: int):
    conn = get_db_connection()
    row = conn.execute(
        "SELECT * FROM landmarks WHERE id = ?", (landmark_id,)
    ).fetchone()
    conn.close()

    if row is None:
        return jsonify({"error": "Landmark not found"}), 404

    landmark = row_to_landmark(row)
    return jsonify(landmark)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
