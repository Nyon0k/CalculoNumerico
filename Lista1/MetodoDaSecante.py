import math
import numpy as np

#Executa o cálculo da função de entrada
def f(x):
    f_result = (x*(math.log10(x)))-1
    return f_result

#Executa o cálculo da função derivada
def derivada(x):
    d_result = math.log10(x)+1/np.log(10)
    return d_result

#Executa o método da bisseção
def secante(x0, x1, err):
    if math.fabs(f(x0)) <= err:
        return x0
    if math.fabs(f(x1)) <= err:
        return x1
    while True:
        x2 = x1-f(x1)*((x1-x0)/(f(x1)-f(x0)))
        if math.fabs(f(abs(x2))) <= err:
            return x2
        x0 = x1
        x1 = x2

##### variaveis pré-definidas #####
a, b = 2, 3 #intervalo [a,b]
x_inicial1, x_inicial2 = 2, 3
err = 1e-7 #tolerancia do erro
print('Raiz aproximada:', secante(x_inicial1, x_inicial2, err))