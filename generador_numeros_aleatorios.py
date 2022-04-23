# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 02:27:45 2021

@author: Julio C. Torreblanca
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import shapiro


"""Inciso a"""
def congruencia_lineal(a:int , c: int, M: int, r0)->list:
    num = [r0]
    for i in range(0, 1000):
        ri = (a* num[i] + c)%M
        num.append(ri)
    return num


"""Inciso b"""
ejemplo2 = congruencia_lineal(57,1,256,10)
print(ejemplo2)
print(f"La frecuancia es 256 ya que a partir de este término se repite")

print("-"*80)
"""Inciso c"""
#Lista con los elementos impares a partir de r_1 hasta r_255
x = [ejemplo2[i] for i in range(1,len(ejemplo2),2)]
#Lista con los elementos pares a partir de r_2 hasta r_256
y = [ejemplo2[i] for i in range(2,len(ejemplo2),2)]

plt.figure(figsize=(6, 6))#Damos tamaño a la figura
plt.plot(x, y, 'r+') #Graficamos los puntos
plt.xlabel('$r_{2i - 1}$',fontsize=20) #nombre del eje x
plt.ylabel('$r_{2i}$',fontsize=20) #nombre del eje y
plt.show() #Mostramos la gráfica


"""Subindice d"""
subindice = [i for i in range(1,len(ejemplo2))] #Creamos la lista de subindices [1,2,...,256] que se usará en el eje x

plt.figure(figsize=(15, 9))#Damos tamaño a la figura
plt.plot(subindice, ejemplo2[1:len(ejemplo2)], 'r*') #Graficamos los puntos
plt.xlabel('Subindice $i$',fontsize=20) #nombre del eje x
plt.ylabel('Numero pseudo-aleatorio $r_{i}$',fontsize=20) #nombre del eje y
plt.show() #Mostramos la gráfica


"""Subindice e"""
# Represento el histograma
plt.hist(ejemplo2, 15, color = "green", ec = "black")
plt.title('Histograma de los numeros generados')
plt.xlabel('Valor de la variab')
plt.ylabel('Frecuencia')
plt.show()
# Prueba de Shapiro-Wilk
estadistico, p_valor = shapiro(ejemplo2)
print(f'Estadisticos = {estadistico:.3}')
print(f'p = {p_valor:.3}')
      
# Interpretación
alpha = 0.05
if p_valor > alpha:
   print('La muestra se aproxima a una distribución Gaussiana o Normal')
else:
   print('La muestra no es una distribución Gaussiana o Normal')


print("-"*80)
"""Subindice f"""
# Represento el histograma
n=1000
x = np.random.rand(n)
plt.hist(x, 50, color = "green", ec = "black")
plt.title(f'Histograma de {n} numeros generados por python')
plt.xlabel('Valor de la variable')
plt.ylabel('Frecuencia')
plt.show()

# Prueba de Shapiro-Wilk
estadistico, p_valor = shapiro(x)
print(f'Estadisticos = {estadistico:.3}')
print(f'p = {p_valor:.3}')
      
# Interpretación
alpha = 0.05
if p_valor > alpha:
   print('La muestra se aproxima a una distribución Gaussiana o Normal')
else:
   print('La muestra no es una distribución Gaussiana o Normal')
