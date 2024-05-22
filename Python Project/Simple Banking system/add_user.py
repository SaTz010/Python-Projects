# password_manager.py

import getpass
from utility import *

PASSWORD_FILE = "passwd.txt"
current_user = None

def add_user():
    '''
    Asks user to input the required credentials to input a new usser 
    '''

    while True:
        passwords = load_passwords()
        
        new_username = input(" New username: ").lower()
        if any(user[0] == new_username for user in passwords):
            print("Sorry! User already exists")
            continue
        
        real_name = input(" Real name: ")
        password = getpass.getpass(" Password: ")  # Masked input
        
        
        encrypted_password = password[::-1]  
        
        passwords.append([new_username, real_name, encrypted_password])
        save_passwords(passwords)
        print("User Registered .")
        break 
    
        

if __name__== "__main__" :
    add_user() 