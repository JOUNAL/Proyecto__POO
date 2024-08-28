i=-1000
numbers=[]

while i <= 1000:
    numbers.append(i)
    i+=1

def negative_value(funcion_deseada):
    for a in numbers:
        g=funcion_deseada.something(x=a)
        if  g <= 0 or g < 0 :
            return g,a
