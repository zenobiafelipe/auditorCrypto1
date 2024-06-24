from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os
import tkinter as tk
from tkinter import filedialog, messagebox
import base64

def decrypt_file():
    try:
        # Seleccionar el documento cifrado (PDF)
        encrypted_document = filedialog.askopenfilename(title="Selecciona el documento cifrado (PDF)", filetypes=(("PDF files", "*.pdf"),))
        if not encrypted_document:
            messagebox.showinfo("Cancelado", "Operación cancelada. No se seleccionó ningún documento.")
            return
        
        # Seleccionar la clave secreta
        secret_key_file = filedialog.askopenfilename(title="Selecciona la clave secreta derivada", filetypes=(("BIN files", "*.bin"),))
        if not secret_key_file:
            messagebox.showinfo("Cancelado", "Operación cancelada. No se seleccionó ninguna clave secreta.")
            return

        # Cargar la clave secreta
        with open(secret_key_file, 'rb') as key_file:
            secret_key = key_file.read()
        print("Clave secreta cargada correctamente.")

        # Leer el contenido del documento cifrado (PDF)
        with open(encrypted_document, 'rb') as file:
            file.seek(0, os.SEEK_END)
            file_size = file.tell()
            file.seek(0)
            encrypted_data_b64 = file.read(file_size - 16).decode('utf-8')

        # Decodificar el texto base64
        encrypted_data = base64.b64decode(encrypted_data_b64)

        # Separar el IV del texto cifrado
        iv = encrypted_data[:16]
        encrypted_data = encrypted_data[16:]

        # Crear un objeto Cipher para AES en modo CBC
        cipher = Cipher(algorithms.AES(secret_key), modes.CBC(iv))
        decryptor = cipher.decryptor()

        # Descifrar el documento
        padded_data = decryptor.update(encrypted_data) + decryptor.finalize()

        # Quitar padding
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        document_data = unpadder.update(padded_data) + unpadder.finalize()

        # Guardar el documento descifrado
        decrypted_document_path = os.path.join("Documentos_Descifrados", os.path.basename(encrypted_document).replace("encrypted_", ""))
        os.makedirs("Documentos_Descifrados", exist_ok=True)
        with open(decrypted_document_path, 'wb') as file:
            file.write(document_data)

        messagebox.showinfo("Éxito", f"Documento descifrado guardado en '{decrypted_document_path}'")
    except Exception as e:
        messagebox.showerror("Error", f"Hubo un problema al descifrar el documento: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    decrypt_document()

