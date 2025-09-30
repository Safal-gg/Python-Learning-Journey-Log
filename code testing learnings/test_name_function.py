import unittest
from name_function import get_formatted_name

class NamesTestClass (unittest.TestCase):
    """Test for name_function.py"""

    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
    
    def test_first_middle_last_name(self):
        formatted_name=get_formatted_name('a','b','c')
        self.assertEqual(formatted_name,'A C B')

if __name__ == '__main__':
    unittest.main()