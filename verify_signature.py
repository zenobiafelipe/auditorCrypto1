from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_public_key
import tkinter as tk
from tkinter import filedialog

def verify_signature():
    public_key_file = filedialog.askopenfilename(title="Selecciona la clave pública RSA", filetypes=(("PEM files", "*.pem"),))
    signed_file = filedialog.askopenfilename(title="Selecciona el archivo firmado")
    signature_file = filedialog.askopenfilename(title="Selecciona el archivo de la firma")

    with open(public_key_file, 'rb') as key_file:
        public_key = load_pem_public_key(key_file.read())

    with open(signed_file, 'rb') as file:
        signed_data = file.read()

    with open(signature_file, 'rb') as file:
        signature = file.read()

    try:
        public_key.verify(
            signature,
            signed_data,
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256()
        )
        print("Firma verificada exitosamente.")
    except Exception as e:
        print("La verificación de la firma falló:", e)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    verify_signature()
