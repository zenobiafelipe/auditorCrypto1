from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization
import os
import tkinter.messagebox as messagebox

def create_dh_keys():
    try:
        parameters = dh.generate_parameters(generator=2, key_size=2048)
        private_key = parameters.generate_private_key()
        public_key = private_key.public_key()

        with open("dh_private_key.pem", "wb") as private_file:
            private_file.write(
                private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.PKCS8,
                    encryption_algorithm=serialization.NoEncryption()
                )
            )

        with open("dh_public_key.pem", "wb") as public_file:
            public_file.write(
                public_key.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo
                )
            )

        messagebox.showinfo("Éxito", "Las claves DH se crearon y guardaron correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"Hubo un problema al crear las claves DH: {e}")

if __name__ == "__main__":
    create_dh_keys()
