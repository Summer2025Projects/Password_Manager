import json
import os


loginInfo = {} 
DATA_FILE = "users_data.json"


def main():  
    global loginInfo
    # Check if the file exists and read the data
    # If the file does not exist, create it
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as file: 
                loginInfo = json.load(file) 
    except (json.JSONDecodeError, FileNotFoundError) as e:
        loginInfo = {}


    status = True
    print("Welcome to the Password Manager")
    # Loop until the user chooses to exit
    while status:
        # Check if the user exists and if not, force register
        print("(1) Create a new account")
        print("(2) Login to an existing account")
        print("(3) Exit")
        choice = input ("Enter yout choice: ")
        match choice:
            case "1":
                username = input("Enter Username: ")
                password = input("Enter Password: ")
                if username in loginInfo:
                    print("Username already exists. Please enter a different username.")
                    while username in loginInfo:
                        username = input("Enter a different Username: ")
                        if username not in loginInfo:
                            loginInfo[username] = password
                            with open(DATA_FILE, "w") as file:
                                json.dump(loginInfo, file, indent=4)
                            print("Yout account has been created.")
                            break
                        print("Username already exists. Please enter a different username.")
                    
                else:
                    loginInfo[username] = password
                    with open(DATA_FILE, "w") as file:
                        json.dump(loginInfo, file, indent=4)
                    print("Yout account has been created.")
            case "2":
                username = input("Enter Username: ")
                password = input("Enter Password: ")
                if username in loginInfo and loginInfo[username] == password:
                    print("Login successful.")
                else:
                    print("Invalid username or password.")
            case "3":
                print("Exiting the program.")
                status = False


    #print("(1) Add new site's information")
        #print("(1) Ask for site name")
        #print("(2) Add new username and password")

    #print("(2) Edit a site's information")
        #print("(1) Change username")
        #print("(2) Change password")

    #print("(3) View list of saved sites")
        # print the key value of the dictionary
        
    #print("(4) Change account username")
        # accessing the first value in the array

    #print("(5) Change account password")
        # accessing the second value in the array
    
    #print("(6) Change between accounts")
        
    
    #print("(7) Delete a site's information")
    
    #print("(X) Exit")
    
    
 
    
   # print("(4) View list of saved passwords")
   # print("(5) Delete saved password")

if __name__ == "__main__":
    main()  