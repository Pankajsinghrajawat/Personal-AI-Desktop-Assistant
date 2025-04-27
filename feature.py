import pyautogui
import time
import sqlite3
import os
from shlex import quote
import psutil
import subprocess

def findContact(name):
    conn = sqlite3.connect('jarvis.db')
    cursor = conn.cursor()
    cursor.execute("SELECT number FROM contacts WHERE lower(name)=?", (name.lower(),))
    result = cursor.fetchone()
    conn.close()
    if result:
        return result[0]
    else:
        return None

def is_whatsapp_open():
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] and "WhatsApp" in proc.info['name']:
            return True
    return False

def open_whatsapp():
    # ✅ Update this path if needed for your system
    subprocess.Popen(["C:\\Users\\DELL\\AppData\\Local\\WhatsApp\\WhatsApp.exe"])
    time.sleep(5)

def send_WhatsApp_message(name, message):
    number = findContact(name)
    if number is None:
        print(f"❌ Contact '{name}' not found in database!")
        return

    if not is_whatsapp_open():
        open_whatsapp()
    else:
        print("✅ WhatsApp already open.")

    # Encode message
    encoded_message = quote(message)
    whatsapp_url = f'whatsapp://send?phone={number}&text={encoded_message}'
    command = f'start "" "{whatsapp_url}"'

    print(f"✅ Opening WhatsApp chat with {name}...")
    os.system(command)

    time.sleep(8)  # Wait for WhatsApp chat to load
    pyautogui.press('enter')  # Press Enter to send
    print(f"✅ Message sent to {name} successfully.")
