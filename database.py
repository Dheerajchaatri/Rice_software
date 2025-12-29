import streamlit as st
import sqlite3

# Get DB connection
def get_db():
    conn = sqlite3.connect("rice.db", check_same_thread=False)
    return conn

# Setup database
def setup_db():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS inventory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        variety TEXT,
        quantity REAL,
        avg_cost REAL
    )
    """)

    conn.commit()
    conn.close()

# Streamlit UI
st.title("Rice Inventory Database")

if st.button("Initialize Database"):
    setup_db()
    st.success("Database & table created successfully")
