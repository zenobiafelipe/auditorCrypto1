from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
import tkinter as tk
from tkinter import filedialog, messagebox

def generate_secret_key():
    try:
        private_key_file = filedialog.askopenfilename(title="Selecciona tu clave privada DH", filetypes=(("PEM files", "*.pem"),))
        if not private_key_file:
            messagebox.showinfo("Cancelado", "Operación cancelada. No se seleccionó ninguna clave privada.")
            return
        
        admin_public_key_file = filedialog.askopenfilename(title="Selecciona la clave pública DH del administrador", filetypes=(("PEM files", "*.pem"),))
        if not admin_public_key_file:
            messagebox.showinfo("Cancelado", "Operación cancelada. No se seleccionó ninguna clave pública.")
            return

        with open(private_key_file, 'rb') as key_file:
            private_key = load_pem_private_key(key_file.read(), password=None)

        with open(admin_public_key_file, 'rb') as key_file:
            admin_public_key = load_pem_public_key(key_file.read())

        shared_key = private_key.exchange(admin_public_key)
        derived_key = HKDF(algorithm=hashes.SHA256(), length=32, salt=None, info=b'handshake data').derive(shared_key)

        with open("derived_secret_key.bin", 'wb') as key_file:
            key_file.write(derived_key)

        messagebox.showinfo("Éxito", "Clave secreta derivada guardada en 'derived_secret_key.bin'")
    except Exception as e:
        messagebox.showerror("Error", f"Hubo un problema al generar la clave secreta: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    generate_secret_key()
