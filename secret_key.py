from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
import tkinter as tk
from tkinter import filedialog

def generate_secret_key():
    private_key_file = filedialog.askopenfilename(title="Selecciona tu clave privada DH", filetypes=(("PEM files", "*.pem"),))
    admin_public_key_file = filedialog.askopenfilename(title="Selecciona la clave pública DH del administrador", filetypes=(("PEM files", "*.pem"),))

    with open(private_key_file, 'rb') as key_file:
        private_key = load_pem_private_key(key_file.read(), password=None)

    with open(admin_public_key_file, 'rb') as key_file:
        admin_public_key = load_pem_public_key(key_file.read())

    shared_key = private_key.exchange(admin_public_key)
    derived_key = HKDF(algorithm=hashes.SHA256(), length=32, salt=None, info=b'handshake data').derive(shared_key)

    with open("derived_secret_key.bin", 'wb') as key_file:
        key_file.write(derived_key)

    print("Clave secreta derivada guardada en 'derived_secret_key.bin'")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    generate_secret_key()
