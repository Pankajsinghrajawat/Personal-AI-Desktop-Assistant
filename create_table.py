import sqlite3

# Database connect
conn = sqlite3.connect('jarvis.db')
cursor = conn.cursor()

# Table create query
cursor.execute("""
CREATE TABLE IF NOT EXISTS contacts(
    name TEXT,
    number TEXT
)
""")

print("Contacts table created successfully!")

conn.commit()
conn.close()
