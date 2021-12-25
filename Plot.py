from ValidationClass import *
import matplotlib.pyplot as plt
class Plot:
    def __init__(self, function, minValue, maxValue):
        self.minvalue=Validation.IsInteger(minValue)
        self.maxValue=Validation.IsInteger(maxValue)
        Validation.InequalityValidation(maxValue,minValue);
        self.func=Validation.ValidateFunction(function)
        
        
        
    def FuncSubstitute(self, x):
        val = eval(self.func)
        return val    
    
    def GenerateFunc(self):
        x_Coor=[]
        y_Coor=[]
        for i in range(self.minvalue,self.maxValue):
            x_Coor.append(i)
            y_Coor.append(self.FuncSubstitute(i))
        return x_Coor,y_Coor
    def plotFunction(self):
        x_Coor, y_Coor = self.GenerateFunc()
        plt.plot(x_Coor, y_Coor, color="red", linewidth=1.5, label=self.func)
        plt.xlabel("X")
        plt.ylabel("F(X)")
        plt.style.use("seaborn-dark")
        plt.show()        
    
        