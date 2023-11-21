from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    return key

def load_key():
    return open("secret.key", "rb").read()

def encrypt_file(file_name, key):
    f = Fernet(key)
    with open(file_name, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open("encrypted_" + file_name, "wb") as file:
        file.write(encrypted_data)

def decrypt_file(file_name, key):
    f = Fernet(key)
    with open(file_name, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open("decrypted_" + file_name, "wb") as file:  
        file.write(decrypted_data)

key = generate_key()

original_file = "foto.jpeg"


encrypt_file(original_file, key)


encrypted_file = "encrypted_" + original_file
decrypt_file(encrypted_file, key)