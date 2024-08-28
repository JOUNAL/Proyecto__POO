from packages.base_function import *
import packages.negatives as ng
abstract=input("Digite la funcion a evaluar:")
Funcion1=MethodsNumerics(desired_function=abstract)
print(Funcion1.inputed_function)
print(ng.negative_value(Funcion1))
print(Funcion1.something(x=2))

def biseccion():
    Xm=Funcion1.something(x=(ng.negative_value(Funcion1)[1]-1))
    Xa=Funcion1.something(x=(ng.negative_value(Funcion1)[1]))
    while (Xa * Xm) < 0:
        Xm=(Xm+Xa)/2
        a=(Xm-Xa)/Xm
        print (Xm)
        print(a)
        if a < 0 :
            a=a*-1
        if a < 0.0001:
            print(a)
            print("Hola")
            return Xm
        
print(biseccion())
