#!/usr/bin/env python3.8
from passwordlocker import User
from passwordlocker import Credential

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
def create_credentialacc(app_name,app_username,app_password):
    '''
    Function to create a new credential account
    '''
    new_credentials = Credential(app_name,app_username,app_password)
    return new_credentials
def save_credentialacc(credentials):
        '''
        Function to save credentialacc
        '''
        credentials.save_credentials()
def delete_credentialacc(credentials):
    '''
    Function to delete a credential account
    '''
    credentials.delete_credentialacc()     

def display_credentialaccs():
    '''
    Function that returns all the saved credential accounts 
    '''
    return Credential.display_credentialaccs()

def main():
        print("*"*80)
        print("                      PASSWORD LOCKER")
        print("""
                Hi,welcome to the password locker app.
                Save all your credentials here!
                """)
        print("What would you like to do?")       
        while True:
                print("Use these short codes : ua - create a new user account, la - login account ex - exit main")
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
                                        while True:

                                                print("Choose one of the following actions:")
                                                print("Use the following short_codes: cnc -create new credentials, sec -save existing credentials,dis -display all credentials ,ex-exit")
                                                short_code=input().lower()
                                                if short_code == "cnc" :
                                                        print("Enter application name")
                                                        app_name = input(">")
                                                        print("Enter application user name") 
                                                        app_username = input(">")
                                                        print ("Enter yes or no if you want the app to generate password for you?") 
                                                        yes_no = input(">").lower()
                                                        if yes_no == "yes" :
                                                                app_password = 665
                                                                
                                                        else :
                                                                print("Enter the application password of your choice")
                                                                app_password = input(">") 
                                                        print(f"Successfully created a passord {app_password} for your {app_name} account")
                                                        save_credentialacc(create_credentialacc(app_name,app_username, app_password)) 

                                                elif short_code == "sec":
                                                        print("Enter application name")
                                                        app_name = input(">")
                                                        print("Enter application user name") 
                                                        app_username = input(">")
                                                        print("Enter password")
                                                        app_password == input(">")
                                                        save_credentialacc(create_credentialacc(app_name,app_username, app_password))
                                                        print(f"Successfully created a passord {app_password} for your {app_name} account")

                                                elif short_code == "dis":
                                                        if display_credentialaccs():
                                                                print("Here is a list of all your contacts")
                                                                for credentials in display_credentialaccs():
                                                                        print(f"Your credentials for your {credentials.app_name} account are: username;{credentials.app_username}and password;{credentials.app_password}")
                                                        else:
                                                                print("There are no saved account credentials yet")
                                                elif short_code == "ex":
                                                        print("Bye .......")
                                                        break
                                                else:
                                                        print("invalid shortcode please try again")
                                else:
                                        print("invalid username or password")
                                        return "la"
                elif short_code == "ex":
                        print("Bye .......")
                        break                        
                else:
                        print("Please enter the short_code above")

if __name__ == '__main__':

    main()