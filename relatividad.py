# -*- coding: utf-8 -*-
#Comenzamos importando las librerías numpy y matplotlib.
import numpy as np
import matplotlib.pyplot as plt

#Creamos un menú
print("""
Factor Gamma de Lorentz

Elija una opción:

1. Gráfica del factor Gamma
2. Calculadora del factor Gamma
""")

opcion = int(input('Opción = '))

# Gráfica del factor Gamma:
# Cuantos más puntos se ingresen, se podrá observar una curva
# más suave así como más puntos cercanos a la velocidad de la luz.
# Prestar atención al término 1-(precision) para evitar dividir
# entre cero
if opcion == 1:
	precision = int(input('''Ingrese la cantidad de puntos
          para la función Gamma: ''')) 
	x=np.linspace(0,1-(precision),precision)
	y=1/np.sqrt(1-x**2)
	plt.plot(x,y)
	plt.show()

# En esta segunda opción podemos calcular el factor Gamma
# al introducir la velocidad como cierto factor de c (vel. de la luz)
elif opcion == 2:
	velocidad = float(input('''Ingrese la velocidad
          como factor de c (por ej. 0.85 significa 85% de c): '''))
	y=1/np.sqrt(1-velocidad**2)
        y= "{0:.3f}".format(y) #para expresar gamma con 3 cifras decimales
	print('El factor Gamma es ',y)
# La idea de usar 'elif' es ir agregando más opciones al menú
# como calculadoras para la dilatación del tiempo o la
# contracción de las longitudes y por supuesto algunas opciones para
# el estudio de la conversión Masa-Energía E=mc^2
else:
	print('Esa opción no está en el menú, hasta luego!')
