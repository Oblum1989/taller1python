"""
***********************************
Autor: Blum
***********************************
funcion : salario_empleado

* Calcula el salario de un empleado a partir de su salario base, horas extras y bonificacion.
* Parametros:
  * salario (list)-->[salario base(float), horas extras(float), bonificacion(float)]

------------------------------------
Retorna:
  (tupla)(valor a pagar con descuentos(float), valor total antes de descuentos(float))
------------------------------------
casos de prueba:
salario = [1000000.0,5.0,0.0]   ===>  (877243.4,1038157.9)
salario = [1500000.25,3.0,1.0]  ===>  (1340881.8,1586842.4)
salario = [0.0,0.0,0.0]         ===>  (0.0, 0.0)
salario = [1.0,1.0,1.0]         ===>  (0.9, 1.0)
------------------------------------
"""
#salario=[salarbiobase,horasextras,bofinicaciones]

def salario_empleado(salario):
  hora_normal=salario[0]/190 # valor de 1 hora de trabajo
  hora_extra=hora_normal*1.45 # valor de 1 hora extra
  v_total_extras=salario[1]*hora_extra
  total_bonificacion=salario[0]*0.035*salario[2] # valor de las bonificaciones

  salario_sin_dsc=salario[0]+v_total_extras+total_bonificacion # salario sin dsctos
  descuestos=salario_sin_dsc*0.155
  salario_final=salario_sin_dsc- descuestos

  return round(salario_final,1),round(salario_sin_dsc,1)

#casos de prueba
salario1 = [1000000.0,5.0,0.0] 
salario2 = [1500000.25,3.0,1.0]
salario3 = [0.0,0.0,0.0]
salario4 = [1.0,1.0,1.0] 
print(salario_empleado(salario1))
print(salario_empleado(salario2))
print(salario_empleado(salario3))
print(salario_empleado(salario4))

"""
**********************************
* Autor: Blum
**********************************
* Funcion: velocidad_media

* La funcion velocidad_media, recibe un arreglo de números enteros, el cual contiene en cada
una de sus posiciones los valores de:
  * La distancia en metros que separa las dos cámaras.
  * La velocidad máxima permitida en ese trayecto en (Km/h).
  * El tiempo en segundos que tarda el conductor en recorrer el trayecto.

* Parametros:
  * conductor(list)
-----------------------------------------------
La función retorna una tupla de dos posiciones:
  *El primer valor representa la velocidad media del trayecto evaluado en (km/h) y con un número decimal.
  * El segundo valor representa sí el conductor debe ser multado o no. Se debe considerar lo siguiente:

  *Imprimirá “OK” si el conductor no superó la velocidad máxima permitida.
  *Imprimirá “MULTA” si se superó la velocidad máxima en menos de un 25% de la velocidad permitida
  *Imprimirá “CURSO” si la velocidad máxima fue superada en un 25% o más de la velocidad permitida.

* Retorna:
  * tupla de dos posiciones

----------------------------------------------
* Casos de prueba:
  conductor = [9165,110,300]    (110.0, OK)
  conductor = [9165,110,299]    (110.3, MULTA)
  conductor = [12000,80,359]    (120.3, CURSO)
  conductor = [-1000,-50,-100]  VALORES NEGATIVOS
-------------------------------------------------
"""

def velocidad_media(conductor):
  distancia = conductor[0]
  v_maxima = conductor[1]
  tiempo = conductor[2]
  v_media = distancia/tiempo * 3.6
  if distancia > 0 and v_maxima > 0 and tiempo > 0:
    if v_media >= v_maxima and (v_media ) < v_maxima + (v_maxima*0.25):
      return (round (v_media,1),"MULTA")
    elif (v_media ) >= v_maxima + (v_maxima*0.25):
      return (round (v_media,1),"CURSO")
    elif v_media < v_maxima and v_media > 0:
      return (round (v_media,1),"OK")
  else:
    return "VALORES NEGATIVOS"
  
  
conductor1 = [9165,110,300]
conductor2 = [9165,110,299]
conductor3 = [12000,80,359]
conductor4 = [-1000,-50,-100]
print(velocidad_media(conductor1))
print(velocidad_media(conductor2))
print(velocidad_media(conductor3))
print(velocidad_media(conductor4))

"""
**********************************
* Autor: Blum
**********************************
* Funcion: tienda_maria

* Realizar una función que reciba como parámetro una lista, el cual contiene en cada una de sus posiciones los
valores de:
  *Una cadena de texto que identifica la operación a realizar. En este caso, las operaciones validas son:
  *ACTUALIZAR, BORRAR y AGREGAR.
  *El código del producto (número entero)
  *El nombre del producto (cadena de texto)
  *El precio del producto (número flotante)
  *Inventario del producto (número entero).

-----------------------------------------------
La función retorna una lista de cuatro posiciones:
  *El primero representará el nombre del producto con el precio mayor
  *El segundo representa el nombre del producto con el precio menor.
  *El tercero representa el promedio de precios (imprimirse con un número decimal)
  *El cuarto representa el valor del inventario (imprimirse con un número decimal)
  *En caso de solicitar ACTUALIZAR o BORRAR un producto que no existe (es decir, que el código del producto no
se encuentra en la base de datos), se debe imprimir “ERROR”. En caso de solicitar AGREGAR un producto cuyo
código ya existe en la base de datos se debe imprimir “ERROR”. Los valores numéricos deben imprimirse con un
número decimal.

----------------------------------------------
* Casos de prueba:
  producto = ['AGREGAR',11,'Melon',70,13]       ===> [Jamon,Melon,5588.2,3504410.0]
  producto = ['BORRAR',10,'Jamon',15000,10]     ===> [Arandanos,Galletas,5600.0,2898500.0]
  producto = ['ACTUALIZAR',7,'Helado',65000,11] ===> [Helado,Galletas,12190.0,4034000.0]
  producto = ['BORRAR',14,'Maiz',45000,12]      ===> ERROR
-------------------------------------------------
"""

def total_inventario(tienda):
    total=0                  
    for clave in tienda.keys():
        total+=tienda[clave][1]*tienda[clave][2]
    return total                                
  
def promedio_precios(tienda):
    promedio=0 
    for clave in tienda.keys(): 
        promedio+=tienda[clave][1] 

    promedio/=len(tienda) 
    return promedio 

def nombre_menor(tienda):
    codigos =list(tienda.keys())  
    menor=tienda[codigos[0]][1] 
    nombre=tienda[codigos[0]][0] 

    for clave in tienda.keys():  
        if tienda[clave][1] < menor:
            menor=tienda[clave][1] 
            nombre=tienda[clave][0]    
    return  nombre

def nombre_mayor(tienda): 
    codigos =list(tienda.keys())  
    mayor=tienda[codigos[0]][1] 
    nombre=tienda[codigos[0]][0] 

    for clave in tienda.keys():   
        if tienda[clave][1] > mayor: 
            mayor=tienda[clave][1] 
            nombre=tienda[clave][0]  
    return  nombre 
     
def agregar_producto(tienda,producto):
    bandera=False
    if  producto[1] in tienda.keys():
        bandera=False
        
    else:
        tienda[producto[1]]=producto[2:5]
        bandera=True
        
    return bandera
 
def actualizar_producto(tienda,producto):
    
    if producto[1] in tienda.keys():
        tienda[producto[1]]=producto[2:5]
        bandera=True
        
    else:
        bandera=False
        
    return bandera


def borrar_producto(tienda,producto):
    bandera=False
    if producto[1] in tienda.keys():
        
        tienda.pop(producto[1])
        bandera=True
        
    else:
        bandera=False
        
    return bandera



def tienda_maria(producto): 
    tienda ={1:['Tangelos',9000.0,67],
            2:['Limones',2500.0,35],
            3:['Peras',2700.0,65],
            4:['Arandanos',9300.0,34],
            5:['Tomates',8100.0,42],
            6:['Fresas',9100.0,90],
            7:['Helado',4500.0,41],
            8:['Galletas',700.0,18],
            9:['Chocolates',4500.0,80],
            10:['Jamon',11000.0,55]}

    if producto[0] == 'AGREGAR':
        bandera=agregar_producto(tienda,producto)
    elif producto[0] == 'ACTUALIZAR':
        bandera=actualizar_producto(tienda,producto)
    elif producto[0] == 'BORRAR':
        bandera=borrar_producto(tienda,producto)
    
    if bandera: 
        y=[nombre_mayor(tienda),nombre_menor(tienda),round(promedio_precios(tienda),1),round(total_inventario(tienda),1)]
    else:
        y='ERROR'
    
    return y


# Casos de prueba
producto1 = ['AGREGAR',11,'Melon',70,13]
producto2 = ['BORRAR',10,'Jamon',15000,10]
producto3 = ['ACTUALIZAR',7,'Helado',65000,11]
producto4 = ['BORRAR',14,'Maiz',45000,12]
print(tienda_maria(producto1))
print(tienda_maria(producto2))
print(tienda_maria(producto3))
print(tienda_maria(producto4))



"""
**********************************
* Autor: Blum
**********************************
* Funcion: copia_examen

* Ejercicio 3: Detectando copia en los exámenes de programación.
Uno de los profesores de programación de la Universidad de Pamplona está comenzando a perder su memoria.
Hace algún tiempo, cuando comenzó a trabajar como docente, no únicamente conocía perfectamente todos los
nombres y apellidos de sus estudiant
* Realizar una función que reciba como parámetro en una lista, el cual contiene en cada una de sus posiciones los
valores de:
  * Un arreglo con las respuestas de cada uno de los exámenes a calificar.
  * Un número entero k, que representa la memoria del profesor.

-----------------------------------------------
La función retorna una tupla de dos posiciones:
  * El primero valor representa el número total de exámenes copiados.
  * El segundo valor representa la cantidad de copias detectadas por el profesor considerando que al calificar
un examen solo es capaz de recordar los k exámenes anteriores.
Dos exámenes se consideran copiados si están representados por el mismo número.
----------------------------------------------
* Casos de prueba:
  examenes  = [[1,2,1,2,1],1]      ==> (3,0)
  examenes  = [[1,2,1,2,1],2]      ==> (3,3)
  examenes  = [[1,2,3,1,2,1],2]    ==> (3,1)
  examenes  = [[1,2,3,4,5,6,7],1]  ==> (0,0)
  examenes  = [[1,1,1,1,1,1,1],2]  ==> (6,6)
-------------------------------------------------
"""

def copia_examen(examenes):
  lista_examenes = examenes[0]
  memoria_profesor = examenes[1]
  copias_encontradas_profesor = 0
  copias_encontradas_total = 0
  for i in range(0, len(lista_examenes)):
    respuesta_examen = lista_examenes[i]
    if (i-memoria_profesor) < 0:
      i_profe = 0 
    else:
      i_profe = i-memoria_profesor

    if respuesta_examen in lista_examenes[(i_profe):i]:
      copias_encontradas_profesor += 1
    if respuesta_examen in lista_examenes[:i]:
      copias_encontradas_total += 1
  return(copias_encontradas_total, copias_encontradas_profesor)

examenes1  = [[1,2,1,2,1],1]    
examenes2  = [[1,2,1,2,1],2]    
examenes3  = [[1,2,3,1,2,1],2] 
examenes4  = [[1,2,3,4,5,6,7],1]
examenes5  = [[1,1,1,1,1,1,1],2]

print(copia_examen(examenes1))
print(copia_examen(examenes2))
print(copia_examen(examenes3))
print(copia_examen(examenes4))
print(copia_examen(examenes5))
