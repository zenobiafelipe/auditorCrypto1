from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_public_key
import tkinter as tk
from tkinter import filedialog, messagebox

def verify_signature():
    try:
        # Seleccionar la clave pública RSA del administrador
        public_key_file = filedialog.askopenfilename(title="Selecciona la clave pública RSA del administrador", filetypes=(("PEM files", "*.pem"),))
        if not public_key_file:
            messagebox.showinfo("Cancelado", "Operación cancelada. No se seleccionó ninguna clave pública.")
            return
        
        # Seleccionar el archivo firmado que contiene tanto el contenido como la firma
        signed_file = filedialog.askopenfilename(title="Selecciona el archivo firmado")
        if not signed_file:
            messagebox.showinfo("Cancelado", "Operación cancelada. No se seleccionó ningún archivo firmado.")
            return

        # Leer la clave pública
        with open(public_key_file, 'rb') as key_file:
            public_key = load_pem_public_key(key_file.read())

        # Leer el archivo firmado (asumimos que el archivo tiene el formato: [contenido][firma])
        with open(signed_file, 'rb') as file:
            signed_data = file.read()
        
        # Asumiendo que los últimos 256 bytes son la firma (esto dependerá del tamaño de la clave)
        content = signed_data[:-256]
        signature = signed_data[-256:]

        # Verificar la firma
        public_key.verify(
            signature,
            content,
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256()
        )
        messagebox.showinfo("Éxito", "Firma verificada exitosamente.")
    except Exception as e:
        messagebox.showerror("Error", f"La verificación de la firma falló: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    verify_signature()
