from cryptography.fernet import Fernet
from base import graphical_getpass, derive_key

def decrypt_file(filename: str, key: bytes) -> None:
    print("Decrypting file...")
    f = Fernet(key)
    with open(filename, "rb") as file:
        file.seek(16)
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data)
    print("File decrypted.")

def decrypt_file_in_memory(filename: str, key: bytes) -> bytes:
    print("Decrypting file in memory...")
    f = Fernet(key)
    with open(filename, "rb") as file:
        file.seek(16)
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    print("File decrypted in memory.")
    return decrypted_data


if __name__ == "__main__":
    password = graphical_getpass("Enter decryption password: ")
    with open("salt.txt", 'rb') as file:
        salt = file.read(16)  # Read 16 bytes for the salt
    key = derive_key(password, salt)
    decrypt_file("data.xlsx", key)