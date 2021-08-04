class User:
    """
    Class that generates new instances of User.
    """

    user_details = [] # Empty contact list

    def __init__(self,first_name,last_name,password,username):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.username = username

    def save_userdetails(self):

        '''
        save_userdetails method saves user's  into user_details
        '''

        User.user_details.append(self)

class Credential:
    """
    Class that generates new instances of Credential.
    """
    credentials = []

    def __init__(self,app_name,app_username,app_password,):
        self.app_name = app_name
        self.app_username = app_username
        self.app_password = app_password

    def save_credentials(self):

        '''
        save_credentials method saves Credential objects into the credentials list
        '''

        Credential.credentials.append(self)

    def delete_credentialacc(self):
        Credential.credentials.remove(self)
