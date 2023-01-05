from cryptography.fernet import Fernet

def key_creator():
    key = Fernet.generate_key()

    with open("key.txt", "wb") as f:
        f.write(key)
