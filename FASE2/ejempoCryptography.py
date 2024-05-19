from cryptography.fernet import Fernet
key = Fernet.generate_key()
cipher_suite = Fernet(key)
cipher_text = cipher_suite.encrypt(b'We are FCFM <3')
plain_text = cipher_suite.decrypt(cipher_text)
print("Texto cifrado:", cipher_text)
print("La llave es:", key)
print("El texto plano es:", plain_text)
