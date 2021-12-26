import re
class Validation:
    
    #validate the function given by user
    def ValidateFunction(func):
        func=func.replace(" ","")
        if func=="":
            raise ValueError("The Functon Field is Empty, Please Enter it")  
            
        toMatch = "(-)?(\d+$)|((-)?(\d+[+-])?(\d+[\*\/])?[xX](\^\d+)?([+-](\d+)?([\*\/][xX](\^\d+)?)?)*)*$"
        matched = re.match(toMatch, func)
        if not matched:
            raise ValueError("Invalid Function")
        func = func.replace('^', '**').replace('X', 'x')
        return func
    
    
    
    #validation function of Max & Min value to check whether they are integers or not 
    def IsInteger(val):
        if val=="":
          raise ValueError("Max and Min Values Should Be Given")

        try:
            num = int(val)
            return num
        except:
            raise ValueError("Please enter Integer Number")
    
    #validate whether the minValue is greater than maxValue or not 
    def InequalityValidation(maxValue,minValue):
        if minValue>=maxValue:
            raise ValueError("Max Value Must be Greater Than MinValue")
   