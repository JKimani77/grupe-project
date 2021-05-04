import unittest
from app.models import Review

class MovieTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''
#id thoughts comments post_id user_id
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_review = Review(1,'Python Must Be Crazy','A thrilling new Python Series',1,1)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_review,Review))