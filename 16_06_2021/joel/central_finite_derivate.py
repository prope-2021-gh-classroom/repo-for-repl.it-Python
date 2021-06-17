# Módulos requeridos.

import numpy as np
import sympy
import math
import matplotlib.pyplot as plt


#recuperado el ejercicio realizado en clase por el profesor


def approx_first_derivative(fun, x, h):
    """
    Numerical differentiation by finite differences. Uses central point formula
    to approximate first derivative of function.
    Args:
        f (function): function definition.
        x (float): point where first derivative will be approximated
        h (float): step size for central differences. Tipically less than 1
    Returns:
        df (float): approximation to first_derivative.
    """
    df = (fun(x+h) - fun(x-h))/(2*h)
    return df

def approx_second_derivative(fun, x, h):
    """
    Numerical differentiation by finite differences. Uses central point formula
    to approximate second derivative of function.
    Args:
        f (function): function definition.
        x (float): point where second derivative will be approximated
        h (float): step size for central differences. Tipically less than 1
    Returns:
        ddf (float): approximation to second_derivative.
    """ 
    ddf =(fun(x+h) - 2.0*fun(x) + fun(x-h))/h**2
    return ddf

def central_approx_diff(f,x,h=0.0001): #el parámetro h tiene un valor default
    df =(f(x+h) - f(x-h))/(2.0*h) #primera derivada
    ddf =(f(x+h) - 2.0*f(x) + f(x-h))/h**2 #segunda derivada
    return df,ddf

def relative_absolute_error(aprox, obj):
    if(np.abs(obj) > 0):
        return np.abs(aprox-obj)/np.abs(obj)
    else:
        return np.abs(aprox-obj)
    
def Rf(f,a,b):
    node=(a+b)/2 #middle point
    h=b-a
    return h*f(node) #polynomial of zero degree

def Rcf(f,a,b,n): #Rcf: composite rectangle method
    """
    Compute numerical approximation using rectangle or mid-point
    method in an interval.
    Nodes are generated via formula: x_i = a+(i+1/2)h_hat for
    i=0,1,...,n-1 and h_hat=(b-a)/n
    Args:
    
        f (float): function expression of integrand.
        
        a (float): left point of interval.
        
        b (float): right point of interval.
        
        n (int): number of subintervals.
        
    Returns:
    
        sum_res (float): numerical approximation to integral
            of f in the interval a,b
    """
    h_hat = (b-a)/n
    sum_res = 0
    for i in range(n):
        x = a+(i+1/2)*h_hat
        sum_res += f(x)
    return h_hat*sum_res



'''    
1) (Tarea) Realizar una gráfica de log(error relativo) vs log(h) (h en el eje horizontal) para aproximar la segunda derivada de $f(x)=e^{-x}$ en $x=1$ con $h \in \{10^{-16}, 10^{-14}, \dots , 10^{-1}\}$ y diferencias hacia delante. Valor a aproximar: $f^{(2)}(1) = e^{-1}$. Usar:

$$\frac{d^2f(x)}{dx} \approx \frac{f(x+2h)-2f(x+h)+f(x)}{h^2}$$


2) Crear un módulo con nombre central_finite_derivative.py en el que se tengan dos funciones de Python que aproximen la primera y segunda derivada de una función en un punto x. Ambas funciones reciben fun, x y h donde: fun es la función a calcularse su primera y segunda derivadas, x es el punto donde se realiza la aproximación y h es el parámetro de espaciado entre x y x+h igual a $h=10^{-6}$. La salida de cada función es un float. Función de prueba: math.atan y x=0.9..

Los nombres de las funciones y sus salidas son:

central_finite_derivative.py	parámetros de entrada	salida
approx_first_derivative	fun (function), x (float) ,h (float)	float
approx_second_derivative	fun (function), x (float), h (float)	float

3) (Tarea) Mismo ejercicio que 2) pero función de prueba: math.asin y x=0.5.
'''


def main():
    
    #Tarea ejercicio uno. grafica el logaritmo
    
    #los valores de prueba
    x, h, f = sympy.symbols("x, h, f")
    f=lambda x: math.exp(-x)
    x= 1
    valores = [1e-16,1e-14,1e-12,1e-10,1e-8,1e-6,1e-4,1e-2,1e-1]
    error = []
    
    #se obtienen las aproximaciones de segunda deriva y el error relativo.
    for h in valores:
        df, ddf = central_approx_diff(f,x,h)
        dd = math.exp(-1)
        sal = relative_absolute_error(ddf, dd)
        error.append(sal)
    
    #Se grafica el logaritmo de las h y los errores relativos
    ejeX = np.array(valores)
    ejeY = np.array(error)
    ejeX = np.log(ejeX)
    ejeY = np.log(ejeY)
     
    
    plt.plot(ejeX,ejeY,'o-')
    plt.xlabel( 'h')
    plt.grid(True) 
    plt.savefig('error_relativo.png',format='png') 
    plt.show() 
    
    
    #Tarea ejercicio tres. math.asin y x=0.5.
    
    #los valores de prueba
    f = math.asin
    h = 1e-6
    x = 0.5
    df, ddf = central_approx_diff(f,x,h)

    print("-"*10)
    print("Aproximación a primera derivada:")
    print(df)
    print("-"*10)
    print("Aproximación a segunda derivada:")
    print(ddf)


    



if __name__ == "__main__":
    main()

