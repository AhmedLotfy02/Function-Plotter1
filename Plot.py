from ValidationClass import *
class Plot:
    def __init__(self, function, minValue, maxValue):
        self.minvalue=Validation.IsInteger(minValue)
        self.maxValue=Validation.IsInteger(maxValue)
        Validation.InequalityValidation(maxValue,minValue);
        self.func=Validation.ValidateFunction(function)