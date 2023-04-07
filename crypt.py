from cryptography.fernet import Fernet
import os

fernet = Fernet(os.environ["KEY"])

with open('cookies.json', 'rb') as file:
    original = file.read()

# encrypting the file
encrypted = fernet.encrypt(original)

# opening the file in write mode and
# writing the encrypted data
with open('cookies2.json', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)