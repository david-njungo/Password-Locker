import unittest # Importing the unittest module
from passwordlocker import User # Importing the contact class
from passwordlocker import Credential

class TestUser(unittest.TestCase):
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User(" "," "," "," ") # create User object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name," ")
        self.assertEqual(self.new_user.last_name," ")
        self.assertEqual(self.new_user.password," ")
        self.assertEqual(self.new_user.username," ")
    def test_save_userdetails(self):
        '''
        test_save_userdetails test case to test if the user object is saved into
         the userdetails list
        '''
        self.new_user.save_userdetails() # saving the new userdetails
        self.assertEqual(len(User.user_details),1)

class TestCredential (unittest.TestCase):
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credentials = Credential(" "," "," ") # create Credential object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credentials.app_name," ")
        self.assertEqual(self.new_credentials.app_username," ")
        self.assertEqual(self.new_credentials.app_password," ")




if __name__ == '__main__':
    unittest.main()
