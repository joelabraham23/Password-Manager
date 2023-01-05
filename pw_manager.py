import sqlite3
import tkinter
from cryptography.fernet import Fernet

def create_db():
    """Only use this functino when it is the first time running
    the password manager"""
    conn = sqlite3.connect("passwordManager.db")
    c = conn.cursor()
    c.execute("CREATE TABLE login_details(website text, username text, password text)")

def display_all():
    """Displays all the records (login details) from the table"""
    pass

def add_pass():
    """Add a new record into the database"""
    pass

def show_pass():
    """Show all the info related to a specifcied record"""
    pass

def delete_pass():
    """Delete a record from the table """
    pass

def modify_pass():
    """Modify the password for a record in table"""
    pass
