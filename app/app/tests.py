from django.test import SimpleTestCase
from app import calc

class CalcTests(SimpleTestCase):
    def test_add_number(self):
        """ test calc module"""
        response = calc.add(5,6)
        self.assertEqual(response, 11)

    def test_subtract(self):
        response = calc.subtract(10, 15)
        self.assertEqual(response, 5)