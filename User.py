class User:
    def __init__(self, name, username, password, list_of_websites):
        self.name = name
        self.username = username
        self.password = password 
        self.list_of_websites = list_of_websites

    def get_name(self):
        return self.name

    def get_username(self):
        return self.username
    
    def get_password(self):
        return self.password
    
    def get_list_of_websites(self):
        return self.list_of_websites
    
    def set_name(self, name):
        self.name = name

    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password 
    
    def set_list_of_websites(self, list_of_websites):
        self.list_of_websites = list_of_websites

    def to_dict(self):
        return {
            "name": self.name,
            "username": self.username,
            "password": self.password,
            "websites": self.list_of_websites
        }

    @classmethod
    def from_dict(cls, dict):
        return cls(
            dict["name"],
            dict["username"],
            dict["password"],
            dict["websites"] 
        )

    