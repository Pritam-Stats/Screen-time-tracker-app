import sqlite3
from datetime import date
import pandas as pd


DB_PATH = "screen_time.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS screen_time (
            date TEXT PRIMARY KEY,
            laptop_time REAL,
            phone_time REAL
        )
    ''')
    conn.commit()
    conn.close()

def add_or_update_entry(entry_date: date, laptop: float, phone: float):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        INSERT INTO screen_time (date, laptop_time, phone_time)
        VALUES (?, ?, ?)
        ON CONFLICT(date) DO UPDATE SET
            laptop_time=excluded.laptop_time,
            phone_time=excluded.phone_time
    ''', (entry_date.isoformat(), laptop, phone))
    conn.commit()
    conn.close()

def fetch_all():
    conn = sqlite3.connect(DB_PATH)
    df = None
    try:
        df = pd.read_sql_query("SELECT * FROM screen_time ORDER BY date", conn, parse_dates=['date'])
    except Exception:
        pass
    conn.close()
    return df
