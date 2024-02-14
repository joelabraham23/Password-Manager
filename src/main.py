"""Password manager utilising sqlite3 
for the database and tkinter to provide a GUI for users."""
from vault.pw_db_manager import create_db, display_all, add_login, show_login, delete_login, modify_login
from cryptography.fernet import Fernet
from vault.key_creator import key_creator
import os


def all():
    '''Function to display all the login details stored in the vault'''
    f_key= Fernet(key)
    # If there is no records in the database
    if len(display_all()) == 0:
        print("\nThere are currently no login details stored in the vault")
    else:
        print("\nThese are all your login details stored in the vault")

    # Displaying all the records in database after decryption of password
    for record in display_all():
        decrypted_pw = f_key.decrypt(record[2]).decode()
        print(f"website='{record[0]}'     username='{record[1]}'     password='{decrypted_pw}'\n")
    print("")

def add():
    '''Function to add a login into the vault'''
    website = input("Enter website: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Encryption of password
    f_key = Fernet(key)
    encoded_password = f_key.encrypt(password.encode())

    add_login(website, username, encoded_password)
    print(f"Login for {website} has been added\n")

def show():
    '''Function to show the login details for a website from the vault'''
    website = input("Enter website: ")
    f_key = Fernet(key)
    # If website provided is not in the database
    if len(show_login(website)) == 0:
        print("This website is not stored in The Vault\n")
    else:
        print(f"Login details for {website}")  
    
    # Looping through the records in database with corresponding website
    for record in show_login(website):
        decrypted_password = f_key.decrypt(record[2]).decode()
        print(f"username='{record[1]}'     password='{decrypted_password}'\n")

def delete():
    '''Function to delete the login details for a website from the vault'''
    website = input("Enter website: ")
    # If website is not stored in database
    if len(show_login(website)) == 0:
        print("This website is not stored in The Vault\n")
    else:
        delete_login(website)
        print(f"This websites login details have been deleted from the vault\n")

def main():
    # If database doesn't exist yet
    try:
        create_db()
    except:
        pass

    # If key file for Fernet encryption does not exist
    if not os.path.exists("key.txt"):
        key_creator()

    # Storing the key for further encryptions
    global key
    key = ""
    with open("key.txt", "rb") as key_file:
        key = key_file.read()


    instructions = """Type an instruction to use your local password manager. Refer to the instructions below if unsure
    'all'  - Display all the login details stored in the vault
    'add'  - Adds a new login detail to the vault
    'show' - Show the login details for a website from the vault
    'del'  - Delete the login details for a website from the vault
    'man'  - Display the manual
    'exit' - Exit the vault"""

    print("Welcome to The Vault!")
    print(instructions)
    while True:
        comm = input("Enter command: ").lower().strip()
        if comm == "exit":
            break
        elif comm == "all":
            all()
        elif comm == "add":
            add()
        elif comm == "show":
            show()
        elif comm == "del":
            delete()
        elif comm == "man":
            print(instructions)
        else:
            print("Invalid command given")
        print(instructions)

if __name__ == "__main__":
    main()
