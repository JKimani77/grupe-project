import unittest
from app.models import Post

class MovieTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_post = Post(1,'Project Posted','Image','post information here',1,'klbbhbh')
#id title image post_info user_id review
    def test_instance(self):
        self.assertTrue(isinstance(self.new_post,Post))