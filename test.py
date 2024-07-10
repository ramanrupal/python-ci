import unittest
from main import to _upper

class MyTestCase(unittest.TestCase):
  def test_to_upper(self):
    name = "Raman"
    upper_name = to_upper(name)
    self.assertEqual(upper_name,"RAMAN")

if __name__ == '__main__':
  unittest.main()
