import json
import os
from User import User
from Website import Website


loginInfo = {} 
DATA_FILE = "users_data.json"


def menu(status):
    # Check if the user exists and if not, force register
    print("(1) Create a new account")
    print("(2) Login to an existing account")
    print("(3) Exit")
    choice = input ("Enter your choice: ")
    match choice:
        case "1":
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            while True:
                if "@" in email and "." in email:
                    break
                else:
                    print("Invalid email. Please enter a valid email address.")
                    email = input("Enter your email: ")
            username = input("Enter Username: ")
            password = input("Enter Password: ")

            if username in loginInfo:
                print("Username already exists. Please enter a different username.")
                while username in loginInfo:
                    username = input("Enter a different Username: ")
                    if username not in loginInfo:
                        user = User(name, email, username, password, [])
                        loginInfo[username] = user
                        with open(DATA_FILE, "w") as file:
                            json.dump({u: user.to_dict() for u, user in loginInfo.items()}, file, indent=4)
                        print("Your account has been created.")
                        menu(status)
                    else:
                        print("Username already exists. Please enter a different username.")
            else:
                user = User(name, email, username, password, [])
                loginInfo[username] = user
                with open(DATA_FILE, "w") as file:
                    json.dump({u: user.to_dict() for u, user in loginInfo.items()}, file, indent=4)
                print("Your account has been created.")
                menu(status)
        case "2":
            print("Login to an existing account")
            print("Please enter your username and password.")
            choice = input("Enter F if you forgot username/password or enter to continue: ").strip().lower()
            if choice == "f":
                print("Please contact support to reset your username/password.")
                status = False
            else:
                status = True
                while True:
                    username = input("Enter Username: ")
                    password = input("Enter Password: ")
                    if username in loginInfo and password == loginInfo[username].get_password():
                        print("Login successful.")
                        loggedIn(loginInfo[username])
                        status = False  
                    else:
                        print("Invalid username or password.")
                        print("Please try again.")
            
                
        case "3":
            print("Exiting the program.")
            status = False
            return status

def loggedIn(user):
    print("(1) Change account username")
    print("(2) Change account password")
    print("(3) Add new site")
    print("(4) Delte a site")
    print("(5) Edit a site's username")
    print("(6) Edit a site's password")
    print("(7) View list of saved sites")
    print("(8) Change between accounts")
    print("(9) Delete Account")
    print("(X) Exit")
    choice = input("Enter your choice: ")

    match choice:
        case "1":
            username = input("Enter a current username: ")
            new_username = input("Enter a new username: ")
            while username == new_username:
                print("New username cannot be the same as the old username.")
                new_username = input("Enter a new username: ")

            if username in loginInfo:
                if new_username in loginInfo:
                    print("Username already exists. Please enter a different username.")
                    while new_username in loginInfo:
                        new_username = input("Enter a different Username: ")
                        if new_username not in loginInfo:
                            user.set_username(new_username)
                            loginInfo[new_username] = loginInfo.pop(username)
                            with open(DATA_FILE, "w") as file:
                                json.dump({u: user.to_dict() for u, user in loginInfo.items()}, file, indent=4)
                            print("Your username has been sucessfully upadated")
                            break
                        print("Username already exists. Please enter a different username.")
                else:
                    user.set_username(new_username)
                    loginInfo[new_username] = loginInfo.pop(username)
                    with open(DATA_FILE, "w") as file:
                        json.dump({u: user.to_dict() for u, user in loginInfo.items()}, file, indent=4)
                    print("Your username has been sucessfully upadated")
                    loggedIn(user)
        case "2":
            password = input("Enter a current password: ")
            new_password = input("Enter a new password: ")
            while password == new_password:
                print("The new password and the old pasword cannot be the same.")
                new_password = input("Enter a new password: ")
            user.set_password(new_password)
            with open(DATA_FILE, "w") as file:
                json.dump({u: user.to_dict() for u, user in loginInfo.items()}, file, indent=4)
            print("Your password has been successfully updated.")
            loggedIn(user)
        case "3":
            site_name =input("Enter the name of the site: ")
            site_username = input("Enter the username for the site: ")
            site_password = input("Enter the password for the site: ")
            site = Website(site_name, site_username, site_password)
            user.get_list_of_websites().append(site)
            with open(DATA_FILE, "w") as file:
                json.dump({u: user.to_dict() for u, user in loginInfo.items()}, file, indent=4)
            print("Site has been added successfully.")
            loggedIn(user)
        case "4":
            site_name = input("Enter the name of the site that you want to delete: ")
            while site_name not in user.get_list_of_wesbsites():
                print("Site not found. Please enter a valid site name.")
                site_name = input("Enter the name of the site that you want to delete: ")
            for site in user.get_list_of_wesbsites():
                if site.get_name() == site_name:
                    user.get_list_of_websites().remove(site)
                    with open(DATA_FILE, "w") as file:
                        json.dump({u: user.to_dict() for u, user in loginInfo.items()}, file, indent=4)
                    print("Site has been deleted successfully.")
                    loggedIn(user)
        case "5":
            site_name = input("Enter the name of the site that you want to edit: ")
            while site_name not in user.get_list_of_websites():
                print("Site not found. Please enter a valid site name.")
                site_name = input("Enter the name of the site that you want to edit: ")
            for site in user.get_list_of_websites():
                if site.get_name() == site_name:
                    new_username = input("Enter the new username for the site: ")
                    site.set_username(new_username)
                    with open(DATA_FILE, "w") as file:
                        json.dump({u: user.to_dict() for u, user in loginInfo.items()}, file, indent=4)
                    print("Site's username has been updated successfully.")
                    loggedIn(user)
        case "6":
            site_name = input("Enter the name of the site that you want to edit: ")
            while site_name not in user.get_list_of_websites():
                print("Site not found. Please enter a valid site name.")
                site_name = input("Enter the name of the site that you want to edit: ")
            for site in user.get_list_of_websites():
                if site.get_name() == site_name:
                    new_password = input("Enter the new password for the site: ")
                    site.set_password(new_password)
                    with open(DATA_FILE, "w") as file:
                        json.dump({u: user.to_dict() for u, user in loginInfo.items()}, file, indent=4)
                    print("Site's password has been updated successfully.")
                    loggedIn(user)
        case "7":
            print("Saved sites, for user: ", user.get_username())
            for site in user.get_list_of_websites():
                print("Name of site:", site.get_name())
        case "8":
            # Change between accounts
            username = input("Enter the username of the account you want to switch to: ")
            while username not in loginInfo:
                print("Username not found. Please enter a valid username.")
                username = input("Enter the username of the account you want to switch to: ")
            if username in loginInfo:
                print("Switching to account:", username)
                loggedIn(loginInfo[username])
                print("You have successfully switched to account:", username)
        case "9":
            username = input("Enter the username of the account you want to delete: ")
            while username not in loginInfo:
                print("Username not found. Please enter a valid username.")
                username = input("Enter the username of the account you want to delete: ")
            del loginInfo[username]
            with open(DATA_FILE, "w") as file:
                json.dump({u: user.to_dict() for u, user in loginInfo.items()}, file, indent=4)
            print("Account has been deleted successfully.")
            loggedIn(user)
        case "X" | "x":
            print("Exiting the program.")
            menu(True)
            
def main():  
    global loginInfo
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as file: 
                data = json.load(file)
                loginInfo = {u: User.from_dict(user) for u, user in data.items()}
    except (json.JSONDecodeError, FileNotFoundError) as e:
        loginInfo = {}

    status = True
    print("Welcome to the Password Manager")
    while status:
        status = menu(status)

if __name__ == "__main__":
    main()  