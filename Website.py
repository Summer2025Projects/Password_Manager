class Website:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
    
    def get_name(self):
        return self.name
    
    #remember to decrypt the username before returning it
    def get_username(self):
        return self.username
    
    #remember to decrypt the password before returning it
    def get_password(self):
        return self.password
    
    def set_name(self, name):
        self.name
    
    #remember to encrypt the username before setting it
    def set_username(self, username):
        self.username = username

    #remember to encrypt the password before setting it
    def set_password(self, password):
        self.password = password
    
    def to_dict(self):
        return {
            "name": self.name,
            "username": self.username,
            "password": self.password
        }