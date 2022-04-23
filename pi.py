# -*- coding: utf-8 -*-
"""

@author: Julio C. Torreblanca
"""
import numpy as np



def experimento_pi(n:int)->float:
    
    """Esta función aproxima a pi usando una relación de proporción entre areas
    y n puntos generados aleatoriamente
    
    
    Parametros
    -----------
        n: int -> numero de puntos a generar aleatoriamente
    
    ----------
    return: float -> es la estimación de pi  
    """              
    m = 0 #numero de puntos dentro de la circunferencia
    x = np.random.rand(n)
    y = np.random.rand(n)
   
    for i in range(n):
    
        z = x[i]**2 + y[i]**2
        if z <= 1:
            m += 1
   
    return (4.0*float(m/n))


def refinamiento_pi(d: float, n = 1000):
    """Esta función estima el valor pi más precisa con un intervalo 
    de confienza
    
    Parametros
    -----------
        n: int -> numero de puntos a generar aleatoriamente
        d: float -> es el valor adecuado para nuestro error cuadratico medio
        
    ------
    return:  -> solo imprime el valor pi con el intervalo de confianza,
                junto con el numero de experimentos hechos
    """
    
    Xj = experimento_pi(n) #obtenemos X1
    j = 1
    Sj = 0
    error_cuadratico = d + 1
    while error_cuadratico >= d:
        Xj1 = Xj + (experimento_pi(n) - Xj)/(j+1) #obtenemos Xj+1
       
        Sj1 = (1 - 1/j)*Sj + (j+1)*(Xj1 - Xj)**2 #obtenemos Sj+1
       
        Xj = Xj1 #guardamos el Xj+1 en Xj el anterior para el siguiente cálculo
        Sj = Sj1 #mismo que arriba
        print(j) #numero de experimentos
        print(Xj) #estimacion de la integral en el experimento j
        error_cuadratico = (Sj/j)**(1/2)
        j += 1
    
    intervalo = 1.96*error_cuadratico # calcula el intervalo de confianza
    print(f"Numero de experimentos realizados: {j}")
    print(f"Estimacion con intervalo de confianza: {Xj:.8} +- {intervalo:e}")
    

refinamiento_pi(10**(-4))
