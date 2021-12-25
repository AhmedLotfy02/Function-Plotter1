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
    
    #def test_Inequality(self):
        #result=ValidationClass.Validation.InequalityValidation(2,3)
        #self.assertFalse(result)
        #result=ValidationClass.Validation.InequalityValidation(5,3)
        #self.assertTrue(result)  
        #result=ValidationClass.Validation.InequalityValidation(3,3)
        #self.assertFalse(result)  
            
        
        
if __name__ == '__main__':
    unittest.main()