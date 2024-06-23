import tkinter as tk
from dh_keys import create_dh_keys
from decrypt import decrypt_file
from secret_key import generate_secret_key
from verify_signature import verify_signature
import webbrowser

def open_cloud_link():
    url = "https://drive.google.com/drive/folders/1yJMHspBXMBjG61aX0QHtrQ4lzLe59SKa?usp=sharing"
    webbrowser.open(url)

def create_interface():
    root = tk.Tk()
    root.title("Interfaz del Auditor")

    tk.Button(root, text="Crear Claves DH", command=create_dh_keys).pack(pady=10)
    tk.Button(root, text="Abrir enlace de la nube", command=open_cloud_link).pack(pady=10)
    tk.Button(root, text="Generar Clave Secreta", command=generate_secret_key).pack(pady=10)
    tk.Button(root, text="Descifrar Archivo", command=decrypt_file).pack(pady=10)
    tk.Button(root, text="Verificar Firma", command=verify_signature).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_interface()
