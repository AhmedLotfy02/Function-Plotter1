
class Validation:
    
    def ValidateFunction(func):
        if func=="":
            raise ValueError("The Functon Field is Empty, Please Enter it")    
    #validation function of Max & Min value to check whether they are integers or not 
    def IsInteger(val):
        if val=="":
          raise ValueError("Max and Min Values Should Be Given")

        try:
            num = int(val)
            return num
        except:
            raise ValueError("Please enter Integer Number")
    
    def InequalityValidation(maxValue,minValue):
        if minValue>=maxValue:
            raise ValueError("Max Value Must be Greater Than MinValue")
   