"""Password manager utilising sqlite3 
for the database and tkinter to provide a GUI for users."""
from pw_db_manager import create_db, display_all, add_login, show_login, delete_login, modify_login
import tkinter
from cryptography.fernet import Fernet


def tk_display_all():
    '''Function to display all the login details on tkinter'''
    # Creating formatting for the GUI
    login_dets_columns = "WEBSITE ------ USERNAME ----- PASSWORD\n"
    columns_label = tkinter.Label(root, text=login_dets_columns)
    columns_label.grid(row=13, column=0, columnspan=2)
    idx = 14
    blank_label = tkinter.Label(root, text='\n').grid(row=idx, column=0, ipadx=100)
    f_key = Fernet(key)
    # Retrieving all the login details and displaying to the GUI
    for record in display_all():
        decrypted_pw = f_key.decrypt(record[2]).decode()
        login_dets_label=tkinter.Label(root, text=f"{record[0]}     {record[1]}     {decrypted_pw}\n")
        login_dets_label.grid(row=idx, column=0, columnspan=2)
        idx+=1


def tk_add_login():
    '''Function to add login details given on tkinter'''
    # Retrieving all the inputs from GUI
    website_input = website_field.get()
    username_input = username_field.get()
    password_input = password_field.get()

    # Encrypting passwords before adding to the db
    f_key = Fernet(key)
    encoded_password = f_key.encrypt(password_input.encode())
    add_login(website_input, username_input, encoded_password)

    # Clearing all input
    website_field.delete(0, tkinter.END)
    username_field.delete(0, tkinter.END)
    password_field.delete(0, tkinter.END)


def tk_show_login():
    '''Function to display a specific login details given its website on tkinter'''
    # Retreiving all input from GUI
    website_input = retrieve_field.get()
    # Decrypting passwords from database
    f_key = Fernet(key)
    # Retrieving all the login details from db and displaying on GUI
    for record in show_login(website_input):
        decrypted_password = f_key.decrypt(record[2]).decode()
        login_dets_label = tkinter.Label(root, text = f"{record[1]}     {decrypted_password}\n")
        login_dets_label.grid(row=8, column=0, columnspan=4, ipadx=100)
    
    # Clearing all previous input
    retrieve_field.delete(0, tkinter.END)

def tk_delete_login():
    '''Function that will Delete a login on tkinter'''
    # Retreiving all input from GUI
    website_input = delete_field.get()
    # Deleting login from db
    delete_login(website_input)
    # Clearing previous input
    delete_field.delete(0, tkinter.END)


# If running password manager for the first time uncomment out this line
try:
    create_db()
except:
    pass

root = tkinter.Tk()
root.title("Password manager")
key = ""
with open("key.txt", "rb") as key_file:
    key = key_file.read()


'''
GUI FORMATTING
'''
welcome_msg = "Welcome!\nPlease enter your username and password along with its corresponding website\n"
welcome_label = tkinter.Label(root, text=welcome_msg)
welcome_label.grid(row=0, column=0, padx=10, pady=20, columnspan=2)


# Create text boxes
website_field = tkinter.Entry(root, width=30)
website_field.grid(row=1, column=1, padx=20)

username_field = tkinter.Entry(root, width=30)
username_field.grid(row=2, column=1, padx=10)

password_field = tkinter.Entry(root, width=30)
password_field.grid(row=3, column=1, padx=10)

# Create text box labels
website_label = tkinter.Label(root, text="Website")
website_label.grid(row=1, column=0)

username_label = tkinter.Label(root, text="Username")
username_label.grid(row=2, column=0)

password_label = tkinter.Label(root, text="Password")
password_label.grid(row=3, column=0)

# Create submit button
submit_button = tkinter.Button(root, text="Add record to password manager", command=tk_add_login)
submit_button.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create white box
white_box = tkinter.Label(root, text="\n").grid(row=8, column=0)

# # Create a query button to show all records
query_button = tkinter.Button(root, text="Show all logins", command=tk_display_all)
query_button.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# Create a button to retrieve a particular record
retrieve_label = tkinter.Label(root, text="Enter website to retrieve credentials for")
retrieve_label.grid(row=5, column=0, columnspan=2, pady=10)

retrieve_field = tkinter.Entry(root, width=30)
retrieve_field.grid(row=6, column=0, columnspan=2)

retrieve_button = tkinter.Button(root, text="Retrieve login for this website", command=tk_show_login)
retrieve_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=120)

# Create a button to delete a particular record
delete_label = tkinter.Label(root, text="Enter website to DELETE credentials for")
delete_label.grid(row=9, column=0, columnspan=2, pady=10)

delete_field = tkinter.Entry(root, width=30)
delete_field.grid(row=10, column=0, columnspan=2)

delete_button = tkinter.Button(root, text="DELETE login for this website", command=tk_delete_login)
delete_button.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=120)

root.mainloop()