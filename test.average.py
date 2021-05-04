#Test for average program 

import unittest 
import average

class testCase(unittest.TestCase):

    def setup(self):
        self.average = average()
    #this test should fail, does not have the right average number 
    def test1(self):
        self.assertEqual(average.calculate([2,4,6]),[4])
    #this test should fail
    def test2(self):
        self.assertEqual(average.calculate([]),(4))
    #this test should pass 
    def test3(self):
        self.assertEqual(average.calculate([12,36]),(24))

if __name__ == "__main__":
    unittest.main()