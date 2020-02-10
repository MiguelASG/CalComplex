import unittest
import calcomplex
import cmath



class TestMyModule(unittest.TestCase):
    
    def test_sum(self):
        su = calcomplex.suma([3,-1],[1,4])
        c1 = complex(3,-1)
        c2 = complex(1,4)
        self.assertEqual(complex(su[0],su[1]), c1+c2)
    def test_sub(self):
        re = calcomplex.resta([3,-1],[1,4])
        c1 = complex(3,-1)
        c2 = complex(1,4)
        self.assertEqual( complex(re[0],re[1]), c1-c2)
    def test_mult(self):
        mu = calcomplex.mult([3,-1],[1,4])
        c1 = complex(3,-1)
        c2 = complex(1,4)
        self.assertEqual( complex(mu[0],mu[1]), c1*c2)
    def test_div(self):
        di = calcomplex.div([3,-1],[1,4])
        c1 = complex(3,-1)
        c2 = complex(1,4)
        self.assertEqual( complex(di[0],di[1]), c1/c2)
    def test_mod(self):
        m = cmath.polar(complex(4,3))
        self.assertEqual(calcomplex.mod([4,3]), m[0])
    def test_conj(self):
        self.assertEqual(calcomplex.conj([3,-1]), [3,1])
    def test_pol(self):
        self.assertEqual(calcomplex.pol([1,1]), [2**(1/2),45]) 
    def test_cart(self):
        self.assertEqual(calcomplex.cart((2**(1/2)) ,45), [1.0,1.0])



        
if __name__ == "__main__":
    unittest.main()
