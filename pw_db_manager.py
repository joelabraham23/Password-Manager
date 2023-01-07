import sqlite3
import tkinter
from cryptography.fernet import Fernet
from key_creator import key_creator

def create_db():
    """Only use this function when it is the first time running
    the password manager"""
    conn = sqlite3.connect("passwordManager.db")
    c = conn.cursor()
    c.execute("CREATE TABLE login_details(website text, username text, password text)")
    key_creator()

def display_all():
    """Displays all the records (login details) from the table"""
    conn = sqlite3.connect("passwordManager.db")
    c = conn.cursor()
    c.execute("SELECT * FROM login_details")
    records = c.fetchall()
    conn.commit()
    conn.close()
    return records


def add_login(website, username, encrypted_password):
    """Add a new record into the database"""
    conn = sqlite3.connect("passwordManager.db")
    c = conn.cursor()

    c.execute("INSERT INTO login_details VALUES (:website, :username, :password)", 
    {
        "website": website, 
        "username": username,
        "password": encrypted_password,
    }
    )
    conn.commit()
    conn.close()


def show_login(website):
    """Show the login details from the table given its website"""
    conn = sqlite3.connect("passwordManager.db")
    c = conn.cursor()

    c.execute("SELECT * FROM login_details WHERE website = (?)",
    (website,))
    items = c.fetchall()
    conn.commit()
    conn.close()
    return items


def delete_login(website):
    """Delete the login details from table given its website """
    conn = sqlite3.connect("passwordManager.db")
    c = conn.cursor()
    c.execute("DELETE FROM login_details where website = (?)",
    (website,))
    conn.commit()
    conn.close()
    

def modify_login():
    """Modify the password for a record in table"""
    pass
