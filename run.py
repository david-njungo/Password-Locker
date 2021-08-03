#!/usr/bin/env python3.8
from passwordlocker import User
def create_account(firstname,lastname,username,password):
        '''
        Function to create a new User
        '''
        new_user = User(firstname,lastname,username,password)
        return new_user

def save_details(user):
        '''
        Function to save userdetails
        '''
        user.save_userdetails()


def main():
        print("*"*80)
        print("                      PASSWORD LOCKER")
        print("""
                Hi,welcome to the password locker account.
                Save all your credentials here!
                """)
        print("What would you like to do?")       
        while True:
                print("Use these short codes : ua - create a new user account, la - login account")
                short_code = input().lower()
                if short_code == "ua":
                                print("Sign in account")
                                print("-"*80)   
                                print("First name ....")
                                first_name=input(">")   
                                print("Last name .....")
                                last_name=input(">")    
                                print("Enter username")
                                username=input(">")    
                                print("Enter password")
                                password=input(">")     
                                save_details(create_account(first_name,last_name,username,password))        
                                print(f"{username} you have successfully created an account proceed to login") 
                elif short_code == "la" :
                                print("Enter username") 
                                userName=input(">") 
                                print ("Enter password") 
                                passWord=input(">")
                                if username == userName and passWord == password:
                                        pass
                                else:
                                        print("invalid username or password")
                                        return "la"

if __name__ == '__main__':

    main()