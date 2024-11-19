import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)
       
    # Add your additional test cases here.
    def test_child_ticket_price1(self):
        self.assertRaises(ValueError, get_ticket_price, -1)
    def test_child_ticket_price2(self):
        self.assertEqual(self.zoo.get_ticket_price(20), 100)
    def test_child_ticket_price3(self):
        self.assertEqual(self.zoo.get_ticket_price(21), 150)
    def test_child_ticket_price4(self):
        self.assertEqual(self.zoo.get_ticket_price(60), 150)
   
    
    
if __name__ == '__main__':
    unittest.main()