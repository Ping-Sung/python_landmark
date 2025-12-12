import sqlite3
import json
from pathlib import Path

DB_NAME = "landmarks.db"
DATA_FILE = Path(__file__).with_name(
    "landmarkData.json")  # 和 init_db.py 放在同一個資料夾


def init_db():
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"找不到 {DATA_FILE.name}，請確認檔案和 init_db.py 在同一個資料夾")

    with DATA_FILE.open(encoding="utf-8") as f:
        data = json.load(f)

    # 連線到 SQLite
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    # 重新建立資料表（測試用：每次重建都會清空舊資料）
    c.execute("DROP TABLE IF EXISTS landmarks")

    c.execute(
        """
        CREATE TABLE landmarks (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT,
            city TEXT,
            state TEXT,
            park TEXT,
            isFeatured INTEGER NOT NULL,
            isFavorite INTEGER NOT NULL,
            description TEXT,
            imageName TEXT,
            latitude REAL,
            longitude REAL
        )
        """
    )

    # 將 JSON 轉成可寫入 SQLite 的格式
    landmarks = []
    for item in data:
        coords = item.get("coordinates", {})
        landmarks.append(
            (
                item["id"],
                item["name"],
                item.get("category"),
                item.get("city"),
                item.get("state"),
                item.get("park"),
                1 if item.get("isFeatured") else 0,
                1 if item.get("isFavorite") else 0,
                item.get("description"),
                item.get("imageName"),
                coords.get("latitude"),
                coords.get("longitude"),
            )
        )

    c.executemany(
        """
        INSERT INTO landmarks
        (id, name, category, city, state, park, isFeatured, isFavorite, description, imageName, latitude, longitude)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        landmarks,
    )

    conn.commit()
    conn.close()
    print(f"Database initialized: {DB_NAME}")
    print(f"Inserted {len(landmarks)} landmarks from {DATA_FILE.name}")


if __name__ == "__main__":
    init_db()
