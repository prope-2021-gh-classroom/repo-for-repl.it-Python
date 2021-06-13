# Módulos requeridos.
import numpy as np  

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

def main():
    #los valores de prueba
    f = np.arctan
    h = 1e-6
    x = 0.9
    res_first_der = approx_first_derivative(f, x, h)
    res_second_der = approx_second_derivative(f, x, h)

    print("Aproximación a primera derivada:")
    print(res_first_der)
    print("-"*10)
    print("Aproximación a segunda derivada:")
    print(res_second_der)


if __name__ == "__main__":
    main()

#main()



