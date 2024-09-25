#Este paquete se encarga de la gestion del metodo de Newton
from packages.base_function import *
def newton(Funcion1,Error_input):
    for points in Funcion1.cut_points:
        Xa=points-1
        b=Funcion1.something(x=Xa)
        c=Funcion1.something_derivated(x=Xa)
        if c==0:
            Xa=points
            b=Funcion1.something(x=Xa)
            c=Funcion1.something_derivated(x=Xa)
        XmNow=Xa-(b/c)
        b=Funcion1.something(x=XmNow)
        c=Funcion1.something_derivated(x=XmNow)
        Xprove=XmNow+0
        XmNow=XmNow-(b/c)
        Error_ad=(XmNow-Xprove)/XmNow
        if Error_ad< 0 :
            Error_ad=Error_ad*-1
        while Error_ad>(Error_input/100):
            while True:
                b=Funcion1.something(x=XmNow)
                c=Funcion1.something_derivated(x=XmNow)
                Xprove=XmNow+0
                XmNow=XmNow-(b/c)
                Error_ad=(XmNow-Xprove)/XmNow
                if Error_ad< 0 :
                    Error_ad=Error_ad*-1
                if Error_ad< (Error_input/100):
                    yield XmNow
                    break
    pass
