from packages.base_function import *
import packages.negatives as ng
abstract=input("Digite la funcion a evaluar:")
Funcion1=MethodsNumerics(desired_function=abstract)
print(Funcion1.inputed_function)
print(ng.negative_value(Funcion1))
print(Funcion1.something(x=2))
Funcion1.cut_points_set(ng.negative_value(Funcion1)[0])



def biseccion():
    for points in Funcion1.cut_points:
        Xf=points
        Xa=points-1
        XmNow=(Xf+Xa)/2
        if (Funcion1.something(x=Xa) * Funcion1.something(x=XmNow)) <0:
            Xf=XmNow+0
        if (Funcion1.something(x=Xf) * Funcion1.something(x=XmNow)) <0:
            Xa=XmNow+0
        XmLast=XmNow+0
        XmNow=(Xf+Xa)/2
        Error_ad=(XmNow-XmLast)/XmNow
        if Error_ad< 0 :
            Error_ad=Error_ad*-1
        while Error_ad>0.01:
            a=Funcion1.something(x=Xf) * Funcion1.something(x=Xa)
            b=Funcion1.something(x=Xf)
            c=Funcion1.something(x=Xa)
            while (Funcion1.something(x=Xf) * Funcion1.something(x=Xa)) < 0:
                XmNow=(Xf+Xa)/2
                if (Funcion1.something(x=Xa) * Funcion1.something(x=XmNow)) <0:
                    Xf=XmNow+0
                if (Funcion1.something(x=Xf) * Funcion1.something(x=XmNow)) <0:
                    Xa=XmNow+0
                XmLast=XmNow+0
                XmNow=(Xf+Xa)/2
                Error_ad=(XmNow-XmLast)/XmNow
                if Error_ad< 0 :
                    Error_ad=Error_ad*-1
                if Error_ad< 0.01 :
                    yield XmNow
                    break




def falsa_posicion():
    return 0
        
for results in biseccion():
    print(results)

