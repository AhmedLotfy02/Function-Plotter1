import unittest
import ValidationClass

class Test(unittest.TestCase):
    def test_IsInteger(self):
        for i in {-10,10}:
            result=ValidationClass.Validation.IsInteger(i);
            self.assertTrue(result)
        
    def test_Func(self):
        result=ValidationClass.Validation.ValidateFunction("2+x")
        self.assertTrue(result)
        result=ValidationClass.Validation.ValidateFunction("2*x+x^2")
        self.assertTrue(result)
        try:
            result=ValidationClass.Validation.ValidateFunction("2//x+x^2")
            print('Passed valid func')
        except ValueError as e:
            self.assertEqual(type(e),ValueError)
            print('Passed valid func')    
        try:
            result=ValidationClass.Validation.ValidateFunction("-2*x+x^2")
            self.assertTrue(result)
            print('Passed valid func')           

        except ValueError as e:
            self.assertEqual(type(e),ValueError)
            print('Passed invalid func')           

        try:
            result=ValidationClass.Validation.ValidateFunction("x+x^2")
            self.assertTrue(result)
            print('Passed valid func')           

        except ValueError as e:
            self.assertEqual(type(e),ValueError) 
            print('Passed invalid func')           

        try:
            result=ValidationClass.Validation.ValidateFunction("x*2+x^2")
            self.assertTrue(result)
            print('Passed valid func')           

        except ValueError as e:
            self.assertEqual(type(e),ValueError) 
            print('Passed invalid func')  
        try:
            result=ValidationClass.Validation.ValidateFunction("3/x+x^2")
            self.assertTrue(result)
            print('Passed valid func')           

        except ValueError as e:
            self.assertEqual(type(e),ValueError) 
            print('Passed invalid func')   
        try:
            result=ValidationClass.Validation.ValidateFunction("3^x+x^2")
            self.assertTrue(result)
            print('Passed valid func')           

        except ValueError as e:
            self.assertEqual(type(e),ValueError) 
            print('Passed invalid func')              
    
    def test_Inequality(self):
        try:
            result=ValidationClass.Validation.InequalityValidation(2,3)

        except ValueError as e:
            self.assertEqual(type(e), ValueError)
       
        result=ValidationClass.Validation.InequalityValidation(5,3)
        self.assertEqual(None,result)  
        try:
             result=ValidationClass.Validation.InequalityValidation(3,3)
        except ValueError as e:
             self.assertEqual(type(e), ValueError)

    
        
    
            
        
        
if __name__ == '__main__':
    unittest.main()