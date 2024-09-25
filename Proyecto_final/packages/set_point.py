def set_point_method(Funcion1,Error_input):
    i=0
    x=0
    deastract=compile(Funcion1,"<string>","eval")
    Xprove=x+0
    x=eval(deastract)
    Error_ad=(x-Xprove)/x
    if Error_ad< 0 :
            Error_ad=Error_ad*-1
    while Error_ad>(Error_input/100):
        deastract=compile(Funcion1,"<string>","eval")
        Xprove=x+0
        x=eval(deastract)
        Error_ad=(x-Xprove)/x
        if Error_ad< 0 :
            Error_ad=Error_ad*-1
        i+=1
        if i==1000:
            a="No se hallo raiz, la ecuacion diverge"
            return a
    return x
    

a="((x**2)-3)/2"
print(set_point_method(a,1))
