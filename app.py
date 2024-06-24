import tkinter as tk
from tkinter import messagebox
import sqlite3
from tkinter import ttk
from PIL import Image, ImageTk

def check_credentials(username, password):
    conn = sqlite3.connect('auditor_app.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
    result = cursor.fetchone()
    conn.close()

    if result:
        return True
    return False

def login():
    username = entry_username.get()
    password = entry_password.get()
    if check_credentials(username, password):
        messagebox.showinfo("Éxito", "Login exitoso.")
        root.destroy()
        from gui import create_interface
        create_interface()
    else:
        messagebox.showerror("Login Failed", "Nombre de usuario o contraseña incorrectos")

def open_new_interface():
    new_interface = tk.Tk()
    new_interface.title("Nueva Interfaz")

    # Contenido de la nueva interfaz
    # Puedes agregar tus widgets aquí

    new_interface.mainloop()

# Crear la ventana de login
root = tk.Tk()
root.title("Login")


# Logo
image_frame = ttk.Frame(root, padding="20 10")
image_frame.pack()

image = Image.open("logo.png")  # Ruta de la imagen
image = image.resize((200, 200), resample=Image.LANCZOS)  # Cambiar tamaño de la imagen con LANCZOS
photo = ImageTk.PhotoImage(image)

image_label = ttk.Label(image_frame, image=photo)
image_label.image = photo
image_label.pack()

# Encabezado
header_label = tk.Label(root, text="Inicio de Sesión", font=("Arial", 16, "bold"))
header_label.pack(pady=10)

# Campos de entrada
tk.Label(root, text="Username").pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

tk.Label(root, text="Password").pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

# Botón de login
tk.Button(root, text="Login", command=login).pack(pady=20)

root.mainloop()
