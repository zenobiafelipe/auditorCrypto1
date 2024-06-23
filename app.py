import tkinter as tk
from tkinter import messagebox
import sqlite3

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

# Crear la ventana de login
root = tk.Tk()
root.title("Login")

tk.Label(root, text="Username").pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

tk.Label(root, text="Password").pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

tk.Button(root, text="Login", command=login).pack(pady=20)

root.mainloop()
