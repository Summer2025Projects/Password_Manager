class User:
    def __init__(self, username, password, list_of_websites):
        self.username = username
        self.password = password 
        self.list_of_websites = list_of_websites

    def get_username(self):
        return self.username
    
    def get_password(self):
        return self.password
    
    def get_list_of_websites(self):
        return self.list_of_websites
    
    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password 
    
    def set_list_of_websites(self, list_of_websites):
        self.list_of_websites = list_of_websites

    