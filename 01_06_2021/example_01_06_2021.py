# Librerias.
import numpy as np 

# Función para calculo de punto medio.
def middle_point(p1, p2):
   #parámetros p1, p2
    return (p1+p2)/2 

# Parametro 1
p1 = 7 
# Parametro 2
p2 = 3.1

m = middle_point(p1, p2)  
#n output with the result


n = middle_point(7, np.pi)
print(m)