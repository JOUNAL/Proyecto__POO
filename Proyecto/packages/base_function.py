import packages.negatives as neg

class MethodsNumerics :
    def __init__(self,desired_function) -> None:
        self.inputed_function=desired_function
        self.cut_points=0

    def something(self,x):
        deastract=compile(self.inputed_function,"<string>","eval")
        output_function=eval(deastract)
        return output_function
    
    def cut_points_set(self,a):
        self.cut_points=a

    









    """class MethodsNumerics :
    def __init__(self,desired_function) -> None:
        self.inputed_function=desired_function

    def something(self):
        deastract=compile(self.inputed_function,"<string>","eval")
        output_function=eval(deastract)
        return output_function


from packages.base_function import *
abstract=input("Digite la funcion a evaluar:")
Funcion1=MethodsNumerics(desired_function=abstract)
print(Funcion1.inputed_function)
print(MethodsNumerics.something())
----------------------------------------------------------------------------------------
def input_function(desired_function,x):
    deastract=compile(desired_function,"<string>","eval")
    output_function=eval(deastract)
    return output_function

from packages.base_function import input_function
abstract=input("Digite la funcion a evaluar:")
print(input_function(abstract,2))"""
