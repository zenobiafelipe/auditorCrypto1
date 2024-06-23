from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import tkinter as tk
from tkinter import filedialog

def decrypt_file():
    private_key_file = filedialog.askopenfilename(title="Selecciona la clave privada DH", filetypes=(("PEM files", "*.pem"),))
    encrypted_file = filedialog.askopenfilename(title="Selecciona el archivo cifrado")

    with open(private_key_file, 'rb') as key_file:
        private_key = load_pem_private_key(key_file.read(), password=None)

    with open(encrypted_file, 'rb') as enc_file:
        encrypted_data = enc_file.read()

    shared_key = private_key.exchange(encrypted_data[:128])  # Assuming the first 128 bytes are the public key
    derived_key = HKDF(algorithm=hashes.SHA256(), length=32, salt=None, info=b'handshake data').derive(shared_key)

    iv = encrypted_data[128:144]
    ciphertext = encrypted_data[144:]

    cipher = Cipher(algorithms.AES(derived_key), modes.CFB(iv))
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()

    output_file = filedialog.asksaveasfilename(title="Guardar archivo descifrado como")
    with open(output_file, 'wb') as file:
        file.write(decrypted_data)

    print(f"Archivo descifrado y guardado como: {output_file}")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    decrypt_file()
