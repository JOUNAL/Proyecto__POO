from packages.base_function import *
i=-1000
numbers=[]

while i <= 1000:
    numbers.append(i)
    i+=1

def negative_value(funcion_deseada):
    ZerosList=[]
    PointsList=[]
    for a in numbers:
        Gbefore=funcion_deseada.something(x=(a-1))
        Gnow=funcion_deseada.something(x=a)
        if Gnow==0:
            ZerosList.append(a)
        if  Gnow*Gbefore<0:
            PointsList.append(a)

    return PointsList,ZerosList