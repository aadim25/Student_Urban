import unittest, calc
class CalcTest(unittest.TestCase):
    def Test_add(self):
        self.assertEqual(calc.summa(1,2),3)

    def Test_sub(self):
        self.assertEqual(calc.sub(1,2),-1)

    def Test_div(self):
        self.assertEqual(calc.div(1,2),0.5)

    def Test_mult(self):
        self.assertEqual(calc.mult(1,2),2)


if __name__=="__main__":
    unittest.main()