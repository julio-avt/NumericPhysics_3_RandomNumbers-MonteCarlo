# -*- coding: utf-8 -*-
"""

@author: Julio C. Torreblanca
"""
import numpy as np

def f1(x):
    return (1-x**2)**(3/2)

def f2(x):
    return 4*np.exp(16*x**2 - 12*x +2)

def experimento(f)->float:
    """Esta función genera n números aleatorios y los evalua
    con la función f para obtener la estimación de la integral en
    [0,1]
    
    Parametros
    -----------
    f: function -> es la funcion a ser integrada
    
    
    ------
    return: float -> es el valor de la integral de f en [0,1]    
    """
    
    n = 100 #cantidad de numeros a generar en [0,1]
    numeros = np.random.rand(n)
    suma = 0.0 #aquí guardaremos las evaluaciones
    
    for x in numeros:
        suma += f(x) 

    return suma/n

def refinamiento(f, d:float):
    """Esta función estima el valor de la integral de forma más precisa con 
    un intervalo de confienza
    
    Parametros
    -----------
    f: function -> es la funcion a ser integrada
    d: float -> es el valor adecuado para nuestro error cuadratico medio
    
    ------
    return:  -> solo imprime el valor de la integral con el intervalo de 
                confianza junto con el numero de iteraciones hechas
    """
    #d = 10**(-4) #valor aceptable
    Xj = experimento(f) #obtenemos X1
    j = 1
    Sj = 0
    error_cuadratico = d + 1
    while error_cuadratico >= d:
        Xj1 = Xj + (experimento(f) - Xj)/(j+1) #obtenemos Xj+1
       
        Sj1 = (1 - 1/j)*Sj + (j+1)*(Xj1 - Xj)**2 #obtenemos Sj+1
       
        Xj = Xj1#guardamos el Xj+1 en Xj el anterior para el siguiente cálculo
        Sj = Sj1 #mismo que arriba
        #print("Experimento: ", j) #numero de experimentos
        #print("Resultado:", Xj) #estimacion de la integral en el experimento j
        error_cuadratico = (Sj/j)**(1/2)
        j += 1
    
    intervalo = 1.96*error_cuadratico # calcula el intervalo de confianza
    print(f"Numero de experimentos realizados: {j}")
    print(f"Estimacion con intervalo de confianza: {Xj:} +- {intervalo:e}")
    
#Calcula la integral 1
print("\nIntegral 1:")       
refinamiento(f1, 10**(-4))
#Calcula la integral 2 
print("\nIntegral 2:")   
refinamiento(f2,10**(-1))    
