import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):

    def setUp(self):
        question='What is your favorite language?'
        self.my_survey=AnonymousSurvey(question)
        self.responses=['English','Nepali','Newari']

    def test_store_response(self):
        
        self.my_survey.store_response('English')
        self.assertIn(self.responses[0],self.my_survey.responses)

    def test_store_three_response(self):
        for response in self.responses:
            self.my_survey.store_response(response)
            
        for response in self.responses:
            self.assertIn(response,self.my_survey.responses)

if __name__=='__main__':
    unittest.main()