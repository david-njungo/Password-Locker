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