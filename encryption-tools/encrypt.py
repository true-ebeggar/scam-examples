import os
from cryptography.fernet import Fernet
from base import graphical_getpass, derive_key

def encrypt_file(filename: str, key: bytes, salt: bytes):
    print("Encrypting file...")
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(salt + encrypted_data)
    print("File encrypted.")

if __name__ == "__main__":
    password = graphical_getpass("Enter encryption password: ")
    salt = os.urandom(16)
    with open("salt.txt", 'wb') as file:
        file.write(salt)
    key = derive_key(password, salt)
    encrypt_file("data.xlsx", key, salt)