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
El metodo de la falsa posicion se podria decir que es una combinación del método de la biseccion, para asegurar que en ese intervalo se encuentra una raiz de la funcion, y el metodo de la secante, intentand
