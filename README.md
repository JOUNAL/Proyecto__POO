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
Estr es sencillo, solo se busca donde la función cambia de signo, se toma ese valor(X1), el valor anterior(X0), y encuentra la mitad entre esos dos puntos, luego verifica si ese punto en la funcion, es negativo o positivo, si es negativo, ese punto medio se vuelve el nuevo X1 y si es positivo, ese valor es el nuevo X0, hasta que se llegué al error deseado, este metodo tiene la peculiariadad de siempre encontrar las raices de una funcion, pero no con una buena precision

## Metodo 2: Metodo de la secante 
