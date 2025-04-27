import sqlite3

# Table banane ka kaam
def createTable():
    conn = sqlite3.connect('jarvis.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (
                        name TEXT,
                        number TEXT
                    )''')
    conn.commit()
    conn.close()

# Contact Add karne ka kaam
def addContact(name, number):
    conn = sqlite3.connect('jarvis.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contacts (name, number) VALUES (?, ?)", (name, number))
    conn.commit()
    conn.close()

# Contact dhoondhne ka kaam
def findContact(name):
    conn = sqlite3.connect('jarvis.db')
    cursor = conn.cursor()
    cursor.execute("SELECT number FROM contacts WHERE name=?", (name,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return result[0]
    else:
        return None
