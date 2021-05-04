#Test for volume of a cube 

import unittest 
import volume

class testCase(unittest.TestCase):

    def setup(self):
        self.volume = volume()
    def test1(self):
        self.assertEqual(volume.calculate(2,1),(8))
    def test2(self):
        self.assertEqual(volume.calculate('x',1), (125))
    def test3(self):
        self.assertEqual(volume.calculate(-3,1),(27))

if __name__ == "__main__":
    unittest.main()