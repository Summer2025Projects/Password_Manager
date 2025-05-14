import json
import os

users = []
DATA_FILE = "users_data.json"


def main(): 
    global users   
    try:
        if os.path.exists(DATA_FILE):  # Ensure the file exists before trying to
            with open(DATA_FILE, "r") as file: 
                users = json.load(file) # skibidi
    except (json.JSONDecodeError, FileNotFoundError) as e:
        users = []  
    name = input("Enter your name")
    users.append(name)
    with open(DATA_FILE, "w") as file:
        json.dump(users, file, indent=4)
    # Create an account or have an existing account    
    #username = input("Enter username")
    #password = input("Enter Password")
    
    # Check if the user exists and if not, force register

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

    print(users)
    



if __name__ == "__main__":
    main()  