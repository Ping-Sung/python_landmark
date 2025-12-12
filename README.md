# Landmarks Backend API (Flask + SQLite)

This repository provides a backend service for delivering landmark data to a client application (for example, a SwiftUI frontend).  
The backend is built with **Flask** and uses **SQLite** as its database.  
Data is imported from `landmarkData.json` and stored in `landmarks.db` through an initialization script.

This back end can be conbined with the following Apple tutorial: https://developer.apple.com/tutorials/swiftui/creating-and-combining-views

Please note the testing data is from the tutorial above.

---

## Features

- RESTful API built using Flask  
- SQLite database with structured landmark records  
- JSON responses fully compatible with SwiftUI `Codable` models  
- Automatic database creation and population from a JSON file  
- CORS support for mobile and web clients  
- Simple and minimal project structure suitable for learning and extension

---


## Installation

### 1. Create and activate a virtual environment and installation

```bash
python3 -m venv venv
source venv/bin/activate
pip install flask flask-cors
```

### 2. Initializing the Database

``` bash
python init_db.py
```

## Running the Server

Start the Flask server (default port: 5001):
``` bash
python app.py
```
expacting output:
 * Running on http://0.0.0.0:5001

Please check if the server is running on...

http://127.0.0.1:5001/landmarks