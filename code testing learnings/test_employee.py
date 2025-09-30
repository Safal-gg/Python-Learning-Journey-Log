import unittest
from Employee import GetEmployee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.salary=GetEmployee('Safal','Shrestha',6000)
    
    def  test_give_default_raise(self):
        self.assertEqual(11000,self.salary.give_raise())

    def  test_give_custom_raise(self):
        self.assertEqual(7000,self.salary.give_raise(1000))

if __name__=='__main__':
    unittest.main()