from packages.base_function import *
import packages.negatives as ng
abstract=input("Digite la funcion a evaluar:")
Funcion1=MethodsNumerics(desired_function=abstract)
print(Funcion1.inputed_function)
print(Funcion1.something(x=2))


print(ng.negative_value(Funcion1))
