import unittest
from impl import PhysicalInfo  

class TestPhysicalInfo(unittest.TestCase):
    def test_invalid_name(self):
        info = PhysicalInfo()
        with self.assertRaises(ValueError):
            info.set_name("123")  
        with self.assertRaises(ValueError):
            info.set_name("Sam!Lo") 
        with self.assertRaises(ValueError):
          info.set_name("A")
        with self.assertRaises(ValueError):
          info.set_name("1234")
        with self.assertRaises(ValueError):
          info.set_name("  ")
        with self.assertRaises(ValueError):
          info.set_name("-")
        with self.assertRaises(ValueError):
          info.set_name("")
        self.assertIsNone(info.get_name())

    def test_invalid_gender(self):
        info = PhysicalInfo()
        with self.assertRaises(ValueError):
          info.set_gender("Male") 

        with self.assertRaises(ValueError):
          info.set_gender("FEMALE")  

        with self.assertRaises(ValueError):
          info.set_gender("m")  

        with self.assertRaises(ValueError):
          info.set_gender("f")  

        with self.assertRaises(ValueError):
          info.set_gender("X") 
        self.assertIsNone(info.get_gender())
    def test_invalid_height(self):
        info = PhysicalInfo()
        with self.assertRaises(ValueError):
          info.set_height(10)  

        with self.assertRaises(ValueError):
          info.set_height(90)  

        with self.assertRaises(ValueError):
          info.set_height(42.5)  

        with self.assertRaises(ValueError):
          info.set_height("60")  

        with self.assertRaises(ValueError):
          info.set_height("sixty")

        self.assertIsNone(info.get_height())

    def test_invalid_temperature(self):
        info = PhysicalInfo()
        with self.assertRaises(ValueError):
          info.set_temperature(94.5)  

        with self.assertRaises(ValueError):
          info.set_temperature(105.0)  

        with self.assertRaises(ValueError):
          info.set_temperature(98)  

        with self.assertRaises(ValueError):
          info.set_temperature("95.9")  

        with self.assertRaises(ValueError):
          info.set_temperature("ninety-five point nine")

        self.assertIsNone(info.get_temperature())

    def test_invalid_date(self):
        info = PhysicalInfo()

        with self.assertRaises(ValueError):
          info.set_date("13-08-2023")  

        with self.assertRaises(ValueError):
          info.set_date("12-32-2023") 

        with self.assertRaises(ValueError):
          info.set_date("12-08-1899")  

        with self.assertRaises(ValueError):
          info.set_date("12-08-2101")  

        with self.assertRaises(ValueError):
          info.set_date("12-08")  

        with self.assertRaises(ValueError):
          info.set_date("2023-08-12") 

        with self.assertRaises(ValueError):
          info.set_date("12/Aug/2023")

        self.assertIsNone(info.get_date())

if __name__ == '__main__':
    unittest.main()