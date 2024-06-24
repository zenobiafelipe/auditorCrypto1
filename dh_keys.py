from cryptography.hazmat.primitives import serialization
import tkinter as tk
import tkinter.messagebox as messagebox

def create_dh_keys():
    try:
        # Cargar los parámetros DH del administrador
        with open("dh_parameters.pem", "rb") as param_file:
            parameters = serialization.load_pem_parameters(param_file.read())

        private_key = parameters.generate_private_key()
        public_key = private_key.public_key()

        with open("dh_auditor_private_key.pem", "wb") as private_file:
            private_file.write(
                private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.PKCS8,
                    encryption_algorithm=serialization.NoEncryption()
                )
            )

        with open("dh_auditor_public_key.pem", "wb") as public_file:
            public_file.write(
                public_key.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo
                )
            )

        messagebox.showinfo("Éxito", "Las claves DH del auditor se crearon y guardaron correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"Hubo un problema al crear las claves DH: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    button = tk.Button(root, text="Crear claves DH", command=create_dh_keys)
    button.pack()
    root.mainloop()
