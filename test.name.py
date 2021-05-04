#Test for full name program 

import unittest 
import fullname

class testCase(unittest.TestCase):

    def setup(self):
        self.fullname = fullname()
    #this test should pass
    def test1(self):
        self.assertEqual(fullname.name("hannah", "maung"),("hannah maung"))
    #this test should pass
    def test2(self):
        self.assertEqual(fullname.name("brandon", "dempsey"), ("brandon dempsey"))
    #this test should fail because of empty string 
    def test3(self):
        self.assertEqual(fullname.name(" ", "b"),("b"))

if __name__ == "__main__":
    unittest.main()