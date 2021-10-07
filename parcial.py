"""
***********************************
funcion : juego

* Se desea construir un juego que cumpla con las siguientes condiciones:
  - Se debe crear un arreglo secuencial de números enteros negativos. (el arreglo debe contener mínimo
    10 elementos).
  - Se debe generar aleatoriamente 5 números enteros (utilizar función randint()), y reemplazar dichos
    valores por cero (0), en el arreglo secuencial, así mismo, generar un arreglo B que almacene los
    elementos que fueron reemplazados.
  - La sumatoria de las posiciones dónde se reemplazó los elementos debe ser un numero impar, para
    ganar el juego
------------------------------------
Retorna:
  - La función retorna una lista de tres (3) posiciones:
  - Posición 0: arreglo secuencial modificado
  - Posición 1: arreglo de números que fueron reemplazados
  - Posición 2: True si se ganó el juego, False si perdió.
------------------------------------
casos de prueba:

------------------------------------
"""
import random
import numpy as np
  
def juego(inicio, fin, salto):
  secuencia_a = list(range(inicio, fin, salto))
  secuencia_b = [0] * 5
  secuencia_final = [0] * 5
  i = 0
  sumatoria = 0
  while i < 5:
    secuencia_b[i] = random.randint(inicio, fin)
    i += 1
  for i in range(0, len(secuencia_b)):
    if (secuencia_b[i] in secuencia_a):
      indice = secuencia_a.index(secuencia_b[i])
      secuencia_final = secuencia_a[indice]
      secuencia_a[indice] = 0
  for i in range(len(secuencia_a)):
    sumatoria += secuencia_a[i]
  if sumatoria % 2 == 0:
      gano=True
  else:
      gano=False

  return [secuencia_a, secuencia_b, gano] 

  
print(juego(-24,-1, 2))
print(juego(-26,-4, 2))
print(juego(-33,-6, 3))


"""
***********************************
funcion : calc_hotel

* Ivaldo está planeando un viaje de vacaciones para él y su familia, debido a la reactivación económica las
opciones de turismo se han ampliado, sin embargo, al analizar con detalle no todas las opciones son viables
debido a que los requerimientos del hospedaje para que Ivaldo y su familia puedan viajar son los siguientes:
- Que tenga 3 o más camas dobles.
- Que tenga 2 o más Piscinas.
- Que el tiempo de viaje en avión no sea superior a 35 minutos.
- Que tenga 4 o más tipos de comida en el plan todo incluido.
------------------------------------
Retorna:
  -La función retorna una lista:
- Cada elemento de la lista representa el precio en dólares del hotel que cumple con las condiciones
anteriormente mencionadas.
- Si no existe ningún registro en la base de datos que cumpla los criterios de Ivaldo, el programa imprimirá
“NO DISPONIBLE”.
------------------------------------
casos de prueba:

------------------------------------
"""

def calc_hotel(hotel):
  arreglo = np.array(hotel)
  total = 0
  for hotel in  arreglo:
    if hotel[0] >= 3 and hotel[1] >= 2 and hotel[2] <= 35 and hotel[3] >= 4:
      total += hotel[4]
  if total != 0:
    return total
  else:
    return "No disponible"

  
hotel = [[2,2,50,4,2900],[3,2,30,4,3050],[2,2,50,4,3350],[2,2,55,3,3100]]
hotel1=[[3,3,40,2,3450],[1,1,25,4,2800],[2,3,25,2,3000],[3,1,25,2,2550],[1,1,25,3,2500],[3,3,40,3,3400]]
print(calc_hotel(hotel))
print(calc_hotel(hotel1))