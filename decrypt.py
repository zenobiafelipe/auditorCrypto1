from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os
import tkinter as tk
from tkinter import filedialog, messagebox
import base64

def decrypt_file():
    try:
        # Seleccionar el archivo cifrado
        encrypted_file_path = filedialog.askopenfilename(title="Selecciona el archivo cifrado", filetypes=(("Encrypted files", "*.enc"),))
        if not encrypted_file_path:
            messagebox.showinfo("Cancelado", "Operación cancelada. No se seleccionó ningún archivo cifrado.")
            return

        # Seleccionar la clave secreta
        secret_key_file = filedialog.askopenfilename(title="Selecciona la clave secreta derivada", filetypes=(("PEM files", "*.pem"),))
        if not secret_key_file:
            messagebox.showinfo("Cancelado", "Operación cancelada. No se seleccionó ninguna clave secreta.")
            return

        # Cargar la clave secreta
        with open(secret_key_file, 'rb') as key_file:
            secret_key = key_file.read()
        print("Clave secreta cargada correctamente.")

        # Leer el contenido del archivo cifrado
        with open(encrypted_file_path, 'rb') as file:
            encrypted_data = file.read()

        # Separar el IV del texto cifrado
        iv = encrypted_data[:16]
        encrypted_data = encrypted_data[16:]

        # Crear un objeto Cipher para AES en modo CBC
        cipher = Cipher(algorithms.AES(secret_key), modes.CBC(iv))
        decryptor = cipher.decryptor()

        # Descifrar el texto
        padded_data = decryptor.update(encrypted_data) + decryptor.finalize()

        # Quitar el padding
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        document_data = unpadder.update(padded_data) + unpadder.finalize()

        # Guardar el archivo descifrado
        decrypted_file_path = os.path.splitext(encrypted_file_path)[0]
        with open(decrypted_file_path, 'wb') as decrypted_file:
            decrypted_file.write(document_data)

        messagebox.showinfo("Éxito", f"Archivo descifrado y guardado en '{decrypted_file_path}'")
    except Exception as e:
        messagebox.showerror("Error", f"Hubo un problema al descifrar el archivo: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    decrypt_file()
