import unittest
import calcomplex
import cmath



class TestMyModule(unittest.TestCase):
    
    def test_sum(self):
        su = calcomplex.suma([3,-1],[1,4])
        c1 = complex(3,-1)
        c2 = complex(1,4)
        self.assertEqual( complex(su[0],su[1]), c1+c2)
    def test_sub(self):
        self.assertEqual(calcomplex.resta([3,-1],[1,4]), [2,-5])
    def test_mult(self):
        self.assertEqual(calcomplex.mult([3,-1],[1,4]), [7,11])
    def test_div(self):
        self.assertEqual(calcomplex.div([-2,1],[1,2]), [0,1])
    def test_mod(self):
        self.assertEqual(calcomplex.mod([4,3]), 5)
    def test_conj(self):
        self.assertEqual(calcomplex.conj([3,-1]), [3,1])
    def test_pol(self):
        self.assertEqual(calcomplex.pol([1,1]), [2**(1/2),45]) 
    def test_cart(self):
        self.assertEqual(calcomplex.cart((2**(1/2)) ,45), [1.0,1.0])



        
if __name__ == "__main__":
    unittest.main()
