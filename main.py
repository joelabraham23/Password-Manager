"""Password manager utilising sqlite3 
for the database and tkinter to provide a GUI for users."""
from pw_db_manager import create_db, display_all, add_login, show_login, delete_login, modify_login
import tkinter
from cryptography.fernet import Fernet

def tk_display_all():
    login_dets_columns = "WEBSITE ------ USERNAME ----- PASSWORD\n"
    columns_label = tkinter.Label(root, text=login_dets_columns)
    columns_label.grid(row=13, column=0, columnspan=2)
    idx = 14
    blank_label = tkinter.Label(root, text='\n').grid(row=idx, column=0, ipadx=100)
    f_key = Fernet(key)
    for record in display_all():
        decrypted_pw = f_key.decrypt(record[2]).decode()
        login_dets_label=tkinter.Label(root, text=f"{record[0]}     {record[1]}     {decrypted_pw}\n")
        login_dets_label.grid(row=idx, column=0, columnspan=2)
        idx+=1


def tk_add_login():
    website_input = website_field.get()
    username_input = username_field.get()
    password_input = password_field.get()

    f_key = Fernet(key)
    encoded_password = f_key.encrypt(password_input.encode())

    add_login(website_input, username_input, encoded_password)
    website_field.delete(0, END)
    username_field.delete(0, END)
    password_field.delete(0, END)


def tk_show_login():
    website_input = website_field.get()
    f_key = Fernet(key)
    for record in show_login(website_input):
        
        decrypted_password = f_key.decrypt(record[2]).decode()
        login_dets_label = tkinter.Label(root, text = f"{record[1]}     {decrypted_password}\n")
        login_dets_label.grid(row=8, column=0, columnspan=4, ipadx=100)
    website_field.delete(0, END)

def tk_delete_login():
    pass

def tk_modify_login():
    pass


# If running password manager for the first time uncomment out this line
create_db()

root = tkinter.Tk()
root.title("Password manager")
key = ""
with open("key.txt", "rb") as key_file:
    key = key_file.read()

