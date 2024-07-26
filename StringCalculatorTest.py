import unittest
from StringCalculator import Add
class TestStringCalculator(unittest.TestCase):
        
        def test_expectZeroForEmptyInput(self):
                self.assertEqual(Add(""), 0)
                
        def test_expectZeroForSingleZero(self):
                self.assertEqual(Add("0"), 0)
                
        def test_expectSumForTwoNumberst(self):
                self.assertEqual(Add("1,2"), 3)
                
        def test_ignoreNumbersGreaterThan1000(self):
                self.assertEqual(Add("1,1001"), 1)
                
        def test_expectSumWithCustomDelimiter(self):
                self.assertEqual(Add("//;\n1;2"), 3)
                
        def test_expectSumWithNewlineDelimiter(self):
                self.assertEqual(Add("1\n2,3"),6);
        




if __name__ == '__main__':
    unittest.main()


