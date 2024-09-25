import tkinter
from packages.base_function import *
from packages.negatives import *
from packages.set_point import *

def get_equation(): #Esta funcion se encarga de poner todas las casillas donde van las raices primero en 0, obtiene los valores de los coeficientes, obtiene las raices de acuardo a cada metodo y pones las raices en las casillas correspondientes
    caja1_a.delete(0,'end')
    caja2_a.delete(0,'end')
    caja3_a.delete(0,'end')
    caja4_a.delete(0,'end')
    caja5_a.delete(0,'end')
    caja6_a.delete(0,'end')
    caja7_a.delete(0,'end')
    caja1_b.delete(0,'end')
    caja2_b.delete(0,'end')
    caja3_b.delete(0,'end')
    caja4_b.delete(0,'end')
    caja5_b.delete(0,'end')
    caja6_b.delete(0,'end')
    caja7_b.delete(0,'end')
    caja1_c.delete(0,'end')
    caja2_c.delete(0,'end')
    caja3_c.delete(0,'end')
    caja4_c.delete(0,'end')
    caja5_c.delete(0,'end')
    caja6_c.delete(0,'end')
    caja7_c.delete(0,'end')
    caja1_d.delete(0,'end')
    caja2_d.delete(0,'end')
    caja3_d.delete(0,'end')
    caja4_d.delete(0,'end')
    caja5_d.delete(0,'end')
    caja6_d.delete(0,'end')
    caja7_d.delete(0,'end')
    vacio["text"]=""
    components_coeficients=[]
    components_coeficients.append(caja1.get())
    components_coeficients.append(caja2.get())
    components_coeficients.append(caja3.get())
    components_coeficients.append(caja4.get())
    components_coeficients.append(caja5.get())
    components_coeficients.append(caja6.get())
    components_coeficients.append(caja7.get())
    error_component=caja8.get()
    Funcion_algo = MethodsNumerics(components_function=components_coeficients,Error=error_component)
    Funcion_algo.construct_function()
    Funcion_algo.construct_derivated_function()
    Funcion_algo.cut_points_set(negative_value(Funcion_algo)[0])
    Funcion_algo.cut_points_sure_set(negative_value(Funcion_algo)[1])
    Funcion_algo.get_roots_bisection()
    Funcion_algo.get_roots_secant()
    Funcion_algo.get_roots_newton()
    Funcion_algo.get_roots_false_position()
    print(Funcion_algo.bisection_roots)
    print(Funcion_algo.secant_roots)
    print(Funcion_algo.newton_roots)
    print(Funcion_algo.false_position_roots)
    if not Funcion_algo.bisection_roots or Funcion_algo.bisection_roots[0]=="x": vacio["text"]="No se encontraron raices" 
    else:
        caja1_a.insert(0,Funcion_algo.bisection_roots[0])
        caja2_a.insert(0,Funcion_algo.bisection_roots[1])
        caja3_a.insert(0,Funcion_algo.bisection_roots[2])
        caja4_a.insert(0,Funcion_algo.bisection_roots[3])
        caja5_a.insert(0,Funcion_algo.bisection_roots[4])
        caja6_a.insert(0,Funcion_algo.bisection_roots[5])
        caja7_a.insert(0,Funcion_algo.bisection_time)
        caja1_b.insert(0,Funcion_algo.secant_roots[0])
        caja2_b.insert(0,Funcion_algo.secant_roots[1])
        caja3_b.insert(0,Funcion_algo.secant_roots[2])
        caja4_b.insert(0,Funcion_algo.secant_roots[3])
        caja5_b.insert(0,Funcion_algo.secant_roots[4])
        caja6_b.insert(0,Funcion_algo.secant_roots[5])
        caja7_b.insert(0,Funcion_algo.secant_time)
        caja1_c.insert(0,Funcion_algo.newton_roots[0])
        caja2_c.insert(0,Funcion_algo.newton_roots[1])
        caja3_c.insert(0,Funcion_algo.newton_roots[2])
        caja4_c.insert(0,Funcion_algo.newton_roots[3])
        caja5_c.insert(0,Funcion_algo.newton_roots[4])
        caja6_c.insert(0,Funcion_algo.newton_roots[5])
        caja7_c.insert(0,Funcion_algo.newton_time)
        caja1_d.insert(0,Funcion_algo.false_position_roots[0])
        caja2_d.insert(0,Funcion_algo.false_position_roots[1])
        caja3_d.insert(0,Funcion_algo.false_position_roots[2])
        caja4_d.insert(0,Funcion_algo.false_position_roots[3])
        caja5_d.insert(0,Funcion_algo.false_position_roots[4])
        caja6_d.insert(0,Funcion_algo.false_position_roots[5])
        caja7_d.insert(0,Funcion_algo.false_position_time)
        pass
    

def get_root_set_point(): #Esta funcion se encarga del metodo del punto fijo, donde se llama a la funcion correspondiente y despues introduce el resultado en la caja de abajo
    caja3_f.delete(0,'end')
    point_set_equation=caja1_f.get()
    point_set_error=eval(caja8_f.get())
    caja3_f.insert(0,set_point_method(Funcion1=point_set_equation,Error_input=point_set_error))


#De aqui en adelante, se genera la GUI para facilitar el uso con el usuario


ventana = tkinter.Tk()
ventana.geometry("1000x660")

texto1 = tkinter.Label(ventana,text="¡Bienvenido!")
texto1.grid(row=0,column=4)

texto2 = tkinter.Label(ventana,wraplength=700,text="Para encontrar las raices del polinomio deseado, digite los coeficientes del polinomio en el orden inidicado a continuacion; A+Bx+Cx²+Dx³+Ex⁴+Fx⁵+Gx⁶, asi mismo como el porcentaje de error que desea en la respuesta(valores mayores a 1 pueden dar lugar a ninguna respuesta)")
texto2.grid(row=1,column=1,columnspan=7)


#Esta parte del codigo se encarga de los coeficientes del polinomio, aqui se digitan y se envian


texto_titulo_1 =tkinter.Label(ventana,text="Coeficientes")
texto_titulo_1.grid(row=3,column=0,columnspan=2,pady=10)

texto3 = tkinter.Label(ventana,text="A:")
texto3.grid(row=5,column=0,pady=4)

caja1= tkinter.Entry(ventana)
caja1.grid(row=5,column=1,pady=4)
caja1.insert(0, '0')


texto4 = tkinter.Label(ventana,text="B:")
texto4.grid(row=6,column=0,pady=4)

caja2= tkinter.Entry(ventana)
caja2.grid(row=6,column=1,pady=4)
caja2.insert(0, '0')


texto5 = tkinter.Label(ventana,text="C:")
texto5.grid(row=7,column=0,pady=4)

caja3= tkinter.Entry(ventana)
caja3.grid(row=7,column=1,pady=4)
caja3.insert(0, '0')


texto6 = tkinter.Label(ventana,text="D:")
texto6.grid(row=8,column=0,pady=4)

caja4= tkinter.Entry(ventana)
caja4.grid(row=8,column=1,pady=4)
caja4.insert(0, '0')


texto7 = tkinter.Label(ventana,text="E:")
texto7.grid(row=9,column=0,pady=4)

caja5= tkinter.Entry(ventana)
caja5.grid(row=9,column=1,pady=4)
caja5.insert(0, '0')


texto8 = tkinter.Label(ventana,text="F:")
texto8.grid(row=10,column=0,pady=4)

caja6= tkinter.Entry(ventana)
caja6.grid(row=10,column=1,pady=4)
caja6.insert(0, '0')


texto9 = tkinter.Label(ventana,text="G:")
texto9.grid(row=11,column=0,pady=4)

caja7= tkinter.Entry(ventana)
caja7.grid(row=11,column=1,pady=4)
caja7.insert(0, '0')


texto9 = tkinter.Label(ventana,text="Error(%):")
texto9.grid(row=12,column=0,pady=4)

caja8= tkinter.Entry(ventana)
caja8.grid(row=12,column=1,pady=4)
caja8.insert(0, 1)


boton1= tkinter.Button(ventana,text="Calcular raices", command=get_equation)
boton1.grid(row=13,column=1,pady=4)


#Esta parte se encarga de mostrar los resultados de mostrar las raices sacadas del primer metodo, y el tiempo que se demoro


texto_titulo_2 =tkinter.Label(ventana,text="Metodo de la biseccion")
texto_titulo_2.grid(row=3,column=2,columnspan=2,pady=10)

texto3_a = tkinter.Label(ventana,text="Raiz 1:")
texto3_a.grid(row=5,column=2,pady=4)

caja1_a= tkinter.Entry(ventana)
caja1_a.grid(row=5,column=3,pady=4)
caja1_a.insert(0, '0')


texto4_a = tkinter.Label(ventana,text="Raiz 2:")
texto4_a.grid(row=6,column=2,pady=4)

caja2_a= tkinter.Entry(ventana)
caja2_a.grid(row=6,column=3,pady=4)
caja2_a.insert(0, '0')


texto5_a = tkinter.Label(ventana,text="Raiz 3:")
texto5_a.grid(row=7,column=2,pady=4)

caja3_a= tkinter.Entry(ventana)
caja3_a.grid(row=7,column=3,pady=4)
caja3_a.insert(0, '0')


texto6_a = tkinter.Label(ventana,text="Raiz 4:")
texto6_a.grid(row=8,column=2,pady=4)

caja4_a= tkinter.Entry(ventana)
caja4_a.grid(row=8,column=3,pady=4)
caja4_a.insert(0, '0')


texto7_a = tkinter.Label(ventana,text="Raiz 5:")
texto7_a.grid(row=9,column=2,pady=4)

caja5_a= tkinter.Entry(ventana)
caja5_a.grid(row=9,column=3,pady=4)
caja5_a.insert(0, '0')
'''caja5_a.config(state="disabled")'''

texto8_a = tkinter.Label(ventana,text="Raiz 6:")
texto8_a.grid(row=10,column=2,pady=4)

caja6_a= tkinter.Entry(ventana)
caja6_a.grid(row=10,column=3,pady=4)
caja6_a.insert(0, '0')


texto9_a = tkinter.Label(ventana,text="Tiempo de ejecucion:")
texto9_a.grid(row=11,column=2,pady=4)

caja7_a= tkinter.Entry(ventana)
caja7_a.grid(row=11,column=3,pady=4)
caja7_a.insert(0, '0')

vacio=tkinter.Label(ventana)
vacio.grid(row=12,column=2,columnspan=2)


#Esta parte se encarga de mostrar los resultados de mostrar las raices sacadas del segundo metodo, y el tiempo que se demoro


texto_titulo_3 =tkinter.Label(ventana,text="Metodo de la secante")
texto_titulo_3.grid(row=3,column=4,columnspan=2,pady=10)

texto3_b = tkinter.Label(ventana,text="Raiz 1:")
texto3_b.grid(row=5,column=4,pady=4)

caja1_b= tkinter.Entry(ventana)
caja1_b.grid(row=5,column=5,pady=4)
caja1_b.insert(0, '0')


texto4_b = tkinter.Label(ventana,text="Raiz 2:")
texto4_b.grid(row=6,column=4,pady=4)

caja2_b= tkinter.Entry(ventana)
caja2_b.grid(row=6,column=5,pady=4)
caja2_b.insert(0, '0')


texto5_b = tkinter.Label(ventana,text="Raiz 3:")
texto5_b.grid(row=7,column=4,pady=4)

caja3_b= tkinter.Entry(ventana)
caja3_b.grid(row=7,column=5,pady=4)
caja3_b.insert(0, '0')


texto6_b = tkinter.Label(ventana,text="Raiz 4:")
texto6_b.grid(row=8,column=4,pady=4)

caja4_b= tkinter.Entry(ventana)
caja4_b.grid(row=8,column=5,pady=4)
caja4_b.insert(0, '0')


texto7_b = tkinter.Label(ventana,text="Raiz 5:")
texto7_b.grid(row=9,column=4,pady=4)

caja5_b= tkinter.Entry(ventana)
caja5_b.grid(row=9,column=5,pady=4)
caja5_b.insert(0, '0')
'''caja5_a.config(state="disabled")'''

texto8_b = tkinter.Label(ventana,text="Raiz 6:")
texto8_b.grid(row=10,column=4,pady=4)

caja6_b= tkinter.Entry(ventana)
caja6_b.grid(row=10,column=5,pady=4)
caja6_b.insert(0, '0')


texto9_b = tkinter.Label(ventana,text="Tiempo de ejecucion:")
texto9_b.grid(row=11,column=4,pady=4)

caja7_b= tkinter.Entry(ventana)
caja7_b.grid(row=11,column=5,pady=4)
caja7_b.insert(0, '0')


#Esta parte se encarga de mostrar los resultados de mostrar las raices sacadas del tercer metodo, y el tiempo que se demoro


texto_titulo_4 =tkinter.Label(ventana,text="Metodo de la newton")
texto_titulo_4.grid(row=3,column=6,columnspan=2,pady=10)

texto3_c = tkinter.Label(ventana,text="Raiz 1:")
texto3_c.grid(row=5,column=6,pady=4)

caja1_c= tkinter.Entry(ventana)
caja1_c.grid(row=5,column=7,pady=4)
caja1_c.insert(0, '0')


texto4_c = tkinter.Label(ventana,text="Raiz 2:")
texto4_c.grid(row=6,column=6,pady=4)

caja2_c= tkinter.Entry(ventana)
caja2_c.grid(row=6,column=7,pady=4)
caja2_c.insert(0, '0')


texto5_c = tkinter.Label(ventana,text="Raiz 3:")
texto5_c.grid(row=7,column=6,pady=4)

caja3_c= tkinter.Entry(ventana)
caja3_c.grid(row=7,column=7,pady=4)
caja3_c.insert(0, '0')


texto6_c = tkinter.Label(ventana,text="Raiz 4:")
texto6_c.grid(row=8,column=6,pady=4)

caja4_c= tkinter.Entry(ventana)
caja4_c.grid(row=8,column=7,pady=4)
caja4_c.insert(0, '0')


texto7_c = tkinter.Label(ventana,text="Raiz 5:")
texto7_c.grid(row=9,column=6,pady=4)

caja5_c= tkinter.Entry(ventana)
caja5_c.grid(row=9,column=7,pady=4)
caja5_c.insert(0, '0')
'''caja5_a.config(state="disabled")'''

texto8_c = tkinter.Label(ventana,text="Raiz 6:")
texto8_c.grid(row=10,column=6,pady=4)

caja6_c= tkinter.Entry(ventana)
caja6_c.grid(row=10,column=7,pady=4)
caja6_c.insert(0, '0')


texto9_c = tkinter.Label(ventana,text="Tiempo de ejecucion:")
texto9_c.grid(row=11,column=6,pady=4)

caja7_c= tkinter.Entry(ventana)
caja7_c.grid(row=11,column=7,pady=4)
caja7_c.insert(0, '0')


#Esta parte se encarga de mostrar los resultados de mostrar las raices sacadas del cuarto metodo, y el tiempo que se demoro


texto_titulo_5 =tkinter.Label(ventana,text="Metodo de la falsa posicion")
texto_titulo_5.grid(row=14,column=0,columnspan=2,pady=10)

texto3_d = tkinter.Label(ventana,text="Raiz 1:")
texto3_d.grid(row=15,column=0,pady=4)

caja1_d= tkinter.Entry(ventana)
caja1_d.grid(row=15,column=1,pady=4)
caja1_d.insert(0, '0')


texto4_d = tkinter.Label(ventana,text="Raiz 2:")
texto4_d.grid(row=16,column=0,pady=4)

caja2_d= tkinter.Entry(ventana)
caja2_d.grid(row=16,column=1,pady=4)
caja2_d.insert(0, '0')


texto5_d = tkinter.Label(ventana,text="Raiz 3:")
texto5_d.grid(row=17,column=0,pady=4)

caja3_d= tkinter.Entry(ventana)
caja3_d.grid(row=17,column=1,pady=4)
caja3_d.insert(0, '0')


texto6_d = tkinter.Label(ventana,text="Raiz 4:")
texto6_d.grid(row=18,column=0,pady=4)

caja4_d= tkinter.Entry(ventana)
caja4_d.grid(row=18,column=1,pady=4)
caja4_d.insert(0, '0')


texto7_d = tkinter.Label(ventana,text="Raiz 5:")
texto7_d.grid(row=19,column=0,pady=4)

caja5_d= tkinter.Entry(ventana)
caja5_d.grid(row=19,column=1,pady=4)
caja5_d.insert(0, '0')
'''caja5_a.config(state="disabled")'''

texto8_d = tkinter.Label(ventana,text="Raiz 6:")
texto8_d.grid(row=20,column=0,pady=4)

caja6_d= tkinter.Entry(ventana)
caja6_d.grid(row=20,column=1,pady=4)
caja6_d.insert(0, '0')


texto9_d = tkinter.Label(ventana,text="Tiempo de ejecucion:")
texto9_d.grid(row=21,column=0,pady=4)

caja7_d= tkinter.Entry(ventana)
caja7_d.grid(row=21,column=1,pady=4)
caja7_d.insert(0, '0')


#Esta parte se encarga de mostrar los resultados de mostrar las raices sacadas del segundo metodo, y el tiempo que se demoro


texto_titulo_6 =tkinter.Label(ventana,text="Metodo del punto fijo(especial)")
texto_titulo_6.grid(row=14,column=4,columnspan=2,pady=10)

texto3_f = tkinter.Label(ventana,text="Ecuacion:")
texto3_f.grid(row=15,column=4,pady=4)

caja1_f= tkinter.Entry(ventana)
caja1_f.grid(row=15,column=5,pady=4)
caja1_f.insert(0, '0')



texto9_f = tkinter.Label(ventana,text="Error(%):")
texto9_f.grid(row=16,column=4,pady=4)

caja8_f= tkinter.Entry(ventana)
caja8_f.grid(row=16,column=5,pady=4)
caja8_f.insert(0, 1)


boton2= tkinter.Button(ventana,text="Calcular raiz", command=get_root_set_point)
boton2.grid(row=17,column=5,pady=4)


texto3_f = tkinter.Label(ventana,text="Resultado:")
texto3_f.grid(row=18,column=4,pady=4)

caja3_f= tkinter.Entry(ventana)
caja3_f.grid(row=18,column=5,pady=4)
caja3_f.insert(0, '0')


ventana.mainloop()
