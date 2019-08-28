# standard libraries
import unittest
import sys

# non-standard libraries

# project libraries
from financial_trading.bonds import simple_bond_valuation

sys.path.insert(1, '/Users/dustin/CS/projects/financial_trading/financial_trading')


class TestPrepData(unittest.TestCase):


    def test_simple_bond_valuation(self):
        '''Tests the simple_bond_valuation function with a variety of examples

        '''

        self.assertLess(simple_bond_valuation(0.04, 0.06, 20) - 77.06, 0.001)


        # testing the types of the output arrays
        self.assertIsInstance(simple_bond_valuation(0.04, 0.06, 20), float)




if __name__ == '__main__':
    unittest.main()