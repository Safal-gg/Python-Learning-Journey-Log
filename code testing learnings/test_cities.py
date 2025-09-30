import unittest
from city_functions import city_info

class CityTest(unittest.TestCase):
    def test_city_info(self):
        info=city_info('Sandiego','Usa',10000)
        self.assertEqual(info,'Sandiego,Usa,Population-10000')

if __name__=='__main__':
    unittest.main()