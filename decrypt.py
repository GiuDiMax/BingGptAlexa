from cryptography.fernet import Fernet
import os

fernet = Fernet(os.environ["KEY"])

with open('cookies.json', 'rb') as enc_file:
    encrypted = enc_file.read()

decrypted = fernet.decrypt(encrypted).decode("utf-8")

print(decrypted)