import sqlite3

def addContact(name, number):
    conn = sqlite3.connect("jarvis.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contacts (name, number) VALUES (?, ?)", (name, number))
    conn.commit()
    conn.close()
    print(f"{name} added successfully!")

# Example
addContact("Ankush", "+917415013904")
addContact("Priyanshi", "+918878744185")
