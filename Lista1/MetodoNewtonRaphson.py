import math as m
import numpy as np

#Executa o cálculo da função de entrada
def f(x):
    f_result = (x*m.log10(x))-1
    return f_result

#Executa o cálculo da função derivada
def derivada(x):
    d_result = m.log10(x)+1/np.log(10)
    return d_result

#Executa o método da bisseção
def newtonRaphson(x_inicial, err):
    x = x_inicial
    while True:
        x_novo = x-(f(x)/derivada(x))
        if abs(f(x_novo)) <= err:
            return x_novo
        x = x_novo

##### variaveis pré-definidas #####
a, b = 2, 3 #intervalo [a,b]
x_inicial = 2
err = 1e-7 #tolerancia do erro
print('Raiz aproximada:', newtonRaphson(x_inicial, err))