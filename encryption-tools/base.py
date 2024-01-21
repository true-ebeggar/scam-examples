import tkinter as tk
from tkinter import simpledialog
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def derive_key(password: str, salt: bytes) -> bytes:
    print("Deriving key...")
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    print("Key derived.")
    return key

def graphical_getpass(prompt="Password: ", title="Input"):
    print(f"Prompting for {title.lower()}...")
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    password = simpledialog.askstring(title, prompt, show='*')
    root.destroy()
    print(f"{title} entered.")
    return password
