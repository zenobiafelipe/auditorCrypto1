import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from dh_keys import create_dh_keys
from decrypt import decrypt_file
from secret_key import generate_secret_key
from verify_signature import verify_signature
import webbrowser
import tkinter.messagebox as messagebox

def open_cloud_link():
    url = "https://drive.google.com/drive/folders/1yJMHspBXMBjG61aX0QHtrQ4lzLe59SKa?usp=sharing"
    webbrowser.open(url)
    messagebox.showinfo("Nube", "Se ha abierto el enlace de la nube en el navegador.")
    
def create_interface():
    root = tk.Tk()
    root.title("Interfaz del Auditor")

    # Encabezado
    header_frame = ttk.Frame(root, padding="20 10")
    header_frame.pack()

    header_label = ttk.Label(header_frame, text="Interfaz del Auditor", font=('Arial', 16, 'bold'))
    header_label.pack()

    # Imagen
    image_frame = ttk.Frame(root, padding="20 10")
    image_frame.pack()

    image = Image.open("logo.png")  # Ruta de la imagen
    image = image.resize((200, 200), resample=Image.LANCZOS)  # Cambiar tamaño de la imagen con LANCZOS
    photo = ImageTk.PhotoImage(image)

    image_label = ttk.Label(image_frame, image=photo)
    image_label.image = photo
    image_label.pack()


    # Otros botones
    ttk.Button(root, text="Crear Claves DH", command=create_dh_keys).pack(pady=10)
    ttk.Button(root, text="Abrir enlace de la nube", command=open_cloud_link).pack(pady=10)
    ttk.Button(root, text="Generar Clave Secreta", command=generate_secret_key).pack(pady=10)
    ttk.Button(root, text="Descifrar Archivo", command=decrypt_file).pack(pady=10)
    ttk.Button(root, text="Verificar Firma", command=verify_signature).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_interface()

