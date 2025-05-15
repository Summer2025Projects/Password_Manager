class Website:
    def __init__(self, website_name, username, password):
        self.website_name = website_name
        self.username = username
        self.password = password
    
    def get_website_name(self):
        return self.website_name
    
    #remember to decrypt the username before returning it
    def get_username(self):
        return self.username
    
    #remember to decrypt the password before returning it
    def get_password(self):
        return self.password
    
    def set_website_name(self, website_name):
        self.website_name
    
    #remember to encrypt the username before setting it
    def set_username(self, username):
        self.username = username

    #remember to encrypt the password before setting it
    def set_password(self, password):
        
        self.password = password