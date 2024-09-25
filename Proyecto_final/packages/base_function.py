import time
import packages.negatives as neg
from packages.biseccion_method import *
from packages.newton_method import *
from packages.secant_method import *
from packages.false_position_method import *

class MethodsNumerics :
    def __init__(self,components_function,Error:float) -> None:
        self.inputed_function=0
        self.derivated_function=0
        self.cut_points=0
        self.A_part=components_function[0]
        self.B_part=components_function[1]
        self.C_part=components_function[2]
        self.D_part=components_function[3]
        self.E_part=components_function[4]
        self.F_part=components_function[5]
        self.G_part=components_function[6]
        self.error=eval(Error)


    def something(self,x):
        deastract=compile(self.inputed_function,"<string>","eval")
        output_function=eval(deastract)
        return output_function
    

    def something_derivated(self,x):
        deastract=compile(self.derivated_function,"<string>","eval")
        output_function=eval(deastract)
        return output_function
    

    def get_roots_bisection(self):
        self.bisection_roots=[]+self.cut_sure_points
        inicio=time.time()
        for results in biseccion(Funcion1=self,Error_input=self.error):
            self.bisection_roots.append(results)
        final=time.time()
        self.bisection_roots.sort()
        while len(self.bisection_roots)<6:
            self.bisection_roots.append("x")
        self.bisection_time=(final-inicio)


    def get_roots_secant(self):
        self.secant_roots=[]+self.cut_sure_points
        inicio=time.time()
        for results in secante(Funcion1=self,Error_input=self.error):
            self.secant_roots.append(results)
        final=time.time()
        self.secant_roots.sort()
        while len(self.secant_roots)<6:
            self.secant_roots.append("x")
        self.secant_time=(final-inicio)
    

    def get_roots_false_position(self):
        self.false_position_roots=[]+self.cut_sure_points
        inicio=time.time()
        for results in false_position(Funcion1=self,Error_input=self.error):
            self.false_position_roots.append(results)
        final=time.time()
        self.false_position_roots.sort()
        while len(self.false_position_roots)<6:
            self.false_position_roots.append("x")
        self.false_position_time=(final-inicio)


    def get_roots_newton(self):
        self.newton_roots=[]+self.cut_sure_points
        inicio=time.time()
        for results in newton(Funcion1=self,Error_input=self.error):
            self.newton_roots.append(results)
        final=time.time()
        self.newton_roots.sort()
        while len(self.newton_roots)<6:
            self.newton_roots.append("x")
        self.newton_time=(final-inicio)
    

    def cut_points_set(self,a):
        self.cut_points=a


    def cut_points_sure_set(self,a):
        self.cut_sure_points=a
    

    def construct_function(self):
        self.inputed_function=(f"{self.A_part}+{self.B_part}*x+{self.C_part}*x**2+{self.D_part}*x**3+{self.E_part}*x**4+{self.F_part}*x**5+{self.G_part}*x**6")


    def construct_derivated_function(self):
        A_derivated=self.B_part
        B_derivated=self.C_part*2
        C_derivated=self.D_part*3
        D_derivated=self.E_part*4
        E_derivated=self.F_part*5
        F_derivated=self.G_part*6
        self.derivated_function=(f"{A_derivated}+{B_derivated}*x+{C_derivated}*x**2+{D_derivated}*x**3+{E_derivated}*x**4+{F_derivated}*x**5")
    









    """class MethodsNumerics :                        CODIGO VIEJO, PARA COMPARAR
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
