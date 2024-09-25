# Proyecto__POO

## Propuesta proyecto
El siguiente proyecto tratara de resolver ecuaciones de maximo (o mas?) grado 6, esto con ayuda de los metodos numericos, que nos ayudan a determinar los valores deseados de una funcion dada, a partir de operaciones aritmeticas sencillas, donde si lo intentaramos por un "despeje basico", se complicaria el problema de manera tal que no podemas pasar de un punto, claro que, esto conlleva un precio, y es que, estas soluciones son aproximaciones con un margen de error a la respuesta real, pero lo suficientemente cercana como para usarla con las necesidades

## Diagrama de clases propuesto
![image](https://github.com/JOUNAL/Proyecto__POO/blob/main/Miscelaneo/Diagrama_proyecto.png)


## Resultado final
El programa permite encontrar las raices de ecuaciones de maximo grado 6 con 5 diferntes metodos numericos, cada uno ofrece una diferente aproximacion sobre el problema y por ende puede ser mas preciso o no segun el problema, todo de acuerdo a las necesidades del usuario, a continuacion se explicara como funciona el programa y como funciona cada metodo numerico

## Funcionalidad: Interfaz Grafica parte 1
Para los primeros cuatro metodos numericos, se necesita ingresar los coeficientes del polinomio como se indica en la parte superior, y tambien el error que requiera el usuario para las raices, luego, se hara click en el boton "Calcular raices", lo cual mostrara los resultados de los primeros 4 metodos y el tiempo de ejecucion de cada uno, si no se encuentra niguna raiz de la ecuacion dada, se le avisara al usuario mediante un texto


## Metodo 1: Metodo de la biseccion
Este es sencillo, solo se busca donde la función cambia de signo, se toma ese valor(X1), el valor anterior(X0), y encuentra la mitad entre esos dos puntos, luego verifica si ese punto en la funcion, es negativo o positivo, si es negativo, ese punto medio se vuelve el nuevo X1 y si es positivo, ese valor es el nuevo X0, hasta que se llegué al error deseado, este metodo tiene la peculiariadad de siempre encontrar las raices de una funcion, pero no con una buena precision

## Metodo 2: Metodo de la secante 
Este metodo se centra en hallar la pendiente entre dos puntos de la funcion, se encuentra la solución oara esa recta donde f(x)=0 y se reemplaza en la ecuación original, este punto se reemplaza por uno de los puntos anteriormente mencionados para hallar la recta y se repite el proceso hasta que se llegue al error deseado

## Metodo 3: Metodo Newton
Aunque el metodo de la secante y el metodo de Newton fueron desarrollados independientemente, ambos usan la pendiente para poder hallar las raices de una ecuacion, el método de Newton aplica directamente la derivada de la funcion, y cada punto nuevo que se vaya encontrando va a ser el reemplazo directo en la ecuacion y lo podra hallar con mayor rapidez

## Metodo 4: Metodo de la falsa posicion
El metodo de la falsa posicion se podria decir que es una combinación del método de la biseccion, para asegurar que en ese intervalo se encuentra una raiz de la funcion, y el metodo de la secante, intentando calcular una pendiente en el intervalo que corte el eje x y que coincida con la ecuación dada

## Metodo 5: Metodo del punto fijo
Este metodo es un tanto peculiar ya que no utiliza la funcion original para hallar sus raices, sino que utiliza una funcion que se halla despejando una de las múltiples variables que hay en la ecuación, para ponerlo en perspectiva, utilizemos la siguiente ecuacion: f(x)=x²-x-3
Y consideramos los siguientes despejes:

```
g(x)=(x+3)/x
h(x)=√(x+3)
j(x)=x²-3
```
En el primer caso se despejo x² al dividir todo entre x,ven el segundo caso se despejo x sacando raiz cuadrado a todo el término restante y el último despeje se hizo restando una x a la ecuacion, y ahora, para hallar las raices, cada ecuacion se evalua en 0 o en un número que no de problemas (como para el caso de g(x)) y el valor que de como resultado se reemplazara de nuevo en la ecuacion, esto se hace N veces, luego se evalua si el comportamiento de todos estos puntos es divergente o convergente, si converge a un valor, ese valor va a ser una de las raices para ecuacion original, lo bueno de este metodo es su precision, ya que los valores a donde convergan son las raices de la funcion original

## Funcionalidad: Interfaz Grafica parte 2
Esta parte va dedicada unicamente al 5to metodo, que debido a la infinidad de despejes que puede llegarva tener una ecuacion de grado 6 dependiendo de los coeficientes que la acompañan, se le pide al usuario que digite un despeje de su ecuacion y si converge, se le dira el valor aproximado de convergencia, sino, se le dira que converge
Para la digitacion de esta ecuacuion hay tres reglas importantes:
1. Toda ecuacion debe estar bien agrupada con parentesis ()
2. Si se desea digitar una potencia, en vez de utilizar el simbolo de potencia normal(^), se debe utilizar el doble asterisco (**)
3. Cada X que vaya precedida por un factor, debe llevar un asterisco (*) entre esta X y el factor



Muchas gracias por leer y espero haya sido de utilidad
