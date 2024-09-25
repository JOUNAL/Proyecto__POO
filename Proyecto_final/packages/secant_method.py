#Este paquete se encarga de la gestion del metodo de la secante
from packages.base_function import *
def secante(Funcion1,Error_input):
    for points in Funcion1.cut_points:
        Xf=points
        Xa=points-1
        b=Funcion1.something(x=Xf)
        c=Funcion1.something(x=Xa)
        XmNow=Xf-(((b*(Xf-Xa))/(b-c)))
        if (Funcion1.something(x=Xa) * Funcion1.something(x=XmNow)) <0:
            Xf=XmNow+0
        if (Funcion1.something(x=Xf) * Funcion1.something(x=XmNow)) <0:
            Xa=XmNow+0
        XmLast=XmNow+0
        b=Funcion1.something(x=Xf)
        c=Funcion1.something(x=Xa)
        XmNow=Xf-(((b*(Xf-Xa))/(b-c)))
        Error_ad=(XmNow-XmLast)/XmNow
        if Error_ad< 0 :
            Error_ad=Error_ad*-1
        while Error_ad>(Error_input/100):
            a=Funcion1.something(x=Xf) * Funcion1.something(x=Xa)
            while (Funcion1.something(x=Xf) * Funcion1.something(x=Xa)) < 0:
                b=Funcion1.something(x=Xf)
                c=Funcion1.something(x=Xa)
                XmNow=Xf-(((b*(Xf-Xa))/(b-c)))
                if (Funcion1.something(x=Xa) * Funcion1.something(x=XmNow)) <0:
                    Xf=XmNow+0
                if (Funcion1.something(x=Xf) * Funcion1.something(x=XmNow)) <0:
                    Xa=XmNow+0
                XmLast=XmNow+0
                XmNow=Xf-(((b*(Xf-Xa))/(b-c)))
                Error_ad=(XmNow-XmLast)/XmNow
                if Error_ad< 0 :
                    Error_ad=Error_ad*-1
                if Error_ad< (Error_input/100) :
                    yield XmNow
                    break
    pass
