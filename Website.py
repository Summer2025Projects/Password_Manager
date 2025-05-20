from cryptography.fernet import Fernet
import os

class Website:
    def __init__(self, name, username, password, key):
        self.name = name
        self.username = username
        self.password = password
        self.key = key
    
    def get_name(self):
        
        return self.name
    
    #remember to decrypt the username before returning it
    def get_username(self):
        return self.decrypt(self.username)
    
    #remember to decrypt the password before returning it
    def get_password(self):
        return self.decrypt(self.password)
    
    def set_name(self, name):
        self.name

    def get_key(self):
        return self.key
    
    #remember to encrypt the username before setting it
    def set_username(self, username):
        self.username = self.encrypt(username)

    #remember to encrypt the password before setting it
    def set_password(self, password):
        self.password = self.encrypt(password)

    def set_key(self, key):
        self.key = key

    def encrypt(self, encrypted_value):
        # Implement encryption logic here
        cipher_suite = Fernet(self.key)
        cipher_text = cipher_suite.encrypt(encrypted_value.encode())
        return cipher_text.decode()

    def decrypt(self, encrypted_value):
        cipher_suite = Fernet(self.key)
        plain_text = cipher_suite.decrypt(encrypted_value.encode()).decode()
        return plain_text
    
    def to_dict(self):
        return {
            "name": self.name,
            "username": self.username,
            "password": self.password,
            "key": self.key
        }