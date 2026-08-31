# database.py - SQLite Connection & Data Access Object
import sqlite3
import hashlib

DB_NAME = "heart_disease.db"

def init_database():
    """Create SQLite tables for users and patient records."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Users Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            role TEXT NOT NULL
        )
    ''')
    
    # Patient Records Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            patient_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER,
            sex INTEGER,
            cp INTEGER,
            trestbps REAL,
            chol REAL,
            fbs INTEGER,
            restecg INTEGER,
            thalach REAL,
            exang INTEGER,
            oldpeak REAL,
            slope INTEGER,
            ca INTEGER,
            thal INTEGER,
            prediction TEXT,
            confidence REAL,
            exam_date TEXT,
            doctor_notes TEXT
        )
    ''')
    
    # Seed default admin user
    default_pwd = hashlib.sha256("admin123".encode()).hexdigest()
    cursor.execute(
        "INSERT OR IGNORE INTO users (username, password_hash, role) VALUES ('admin', ?, 'Admin')",
        (default_pwd,)
    )
    
    conn.commit()
    conn.close()

def verify_user(username, password, role):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    pwd_hash = hashlib.sha256(password.encode()).hexdigest()
    
    cursor.execute(
        "SELECT id FROM users WHERE username=? AND password_hash=? AND role=?",
        (username, pwd_hash, role)
    )
    row = cursor.fetchone()
    conn.close()
    
    return (True, row[0]) if row else (False,None)
