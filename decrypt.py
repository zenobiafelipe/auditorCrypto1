from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os
import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2

def decrypt_file():
    try:
        # Seleccionar el documento cifrado (.pdf)
        encrypted_document_path = filedialog.askopenfilename(title="Selecciona el documento cifrado", filetypes=(("PDF files", "*.pdf"),))
        if not encrypted_document_path:
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

        # Leer el contenido del archivo cifrado
        with open(encrypted_document_path, 'rb') as file:
            iv = file.read(16)  # Leer el IV (primeros 16 bytes)
            encrypted_data = file.read()  # Leer el texto cifrado restante

        # Crear un objeto Cipher para AES en modo CBC
        cipher = Cipher(algorithms.AES(secret_key), modes.CBC(iv))
        decryptor = cipher.decryptor()

        # Descifrar los datos
        padded_data = decryptor.update(encrypted_data) + decryptor.finalize()

        # Quitar el padding del documento
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        document_data = unpadder.update(padded_data) + unpadder.finalize()

        # Guardar el documento descifrado temporalmente
        decrypted_document_path = os.path.join("Documentos_Descifrados", os.path.basename(encrypted_document_path).replace(".pdf.enc", ".pdf"))
        os.makedirs("Documentos_Descifrados", exist_ok=True)
        with open(decrypted_document_path, 'wb') as file:
            file.write(document_data)

        # Leer y mostrar el contenido del documento PDF descifrado
        with open(decrypted_document_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfFileReader(file)
            for page_num in range(pdf_reader.numPages):
                page = pdf_reader.getPage(page_num)
                print(page.extract_text())

        messagebox.showinfo("Éxito", f"Documento descifrado y guardado en '{decrypted_document_path}'")
    except Exception as e:
        messagebox.showerror("Error", f"Hubo un problema al descifrar el documento: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    decrypt_file()
