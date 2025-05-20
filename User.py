from Website import Website

class User:
    def __init__(self, name, email, username, password, list_of_websites, access):
        self.name = name
        self.email = email
        self.username = username
        self.password = password 
        self.list_of_websites = list_of_websites
        self.access = access
    

    def get_name(self):
        return self.name
    
    def get_email(self):
        return self.email

    def get_username(self):
        return self.username
    
    def get_password(self):
        return self.password
    
    def get_list_of_websites(self):
        return self.list_of_websites
    
    def get_access(self):
        return self.access
    
    def set_name(self, name):
        self.name = name
    
    def set_email(self, email):
        self.email = email

    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password 
    
    def set_list_of_websites(self, list_of_websites):
        self.list_of_websites = list_of_websites

    def set_access(self, access):
        self.access = access

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "username": self.username,
            "password": self.password,
            "websites": [site.to_dict() for site in self.list_of_websites],
            "access": self.access
        }

    @classmethod
    def from_dict(cls, data):
        websites = [Website(**site) for site in data.get("websites", [])]
        return cls(
            data["name"],
            data["email"],
            data["username"],
            data["password"],
            websites,
            data.get("access", False)
        )

    