import math as m
import numpy as np

dados = [] #salvar iterações e |f(Raiz)|

#Executa o cálculo da função de entrada
def f(x):
    f_result = (x*m.log10(x))-1 #função questão 1
    # f_result = (x**3)-2*(x**2)-11*x+12 #outra função que converge
    # f_result = np.cbrt(x) #função que diverge
    return f_result

#Executa o cálculo da função derivada
def derivada(x):
    d_result = m.log10(x)+1/np.log(10)
    # d_result = 3*(x**2)-4*x-11 #derivada da outra função que converge
    # d_result = 1/(3*x**(2/3)) #derivada da função que diverge
    return d_result

#Executa o método da bisseção
def newtonRaphson(x_inicial, err, iteracao):
    x = x_inicial
    cont = 0
    while True:
        cont += 1
        x_novo = x-(f(x)/derivada(x_inicial))
        if abs(f(x_novo)) <= err:
            dados.append(cont)
            dados.append(abs(f(x_novo)))
            return x_novo
        if cont == iteracao:
            print('Iteração máxima estourada.')
            return False
        x = x_novo

##### variaveis pré-definidas #####
a, b = 2, 3 #intervalo [a,b]
x_inicial = 2
err = 1e-7 #tolerancia do erro
iteracao = 100
raiz = newtonRaphson(x_inicial, err, iteracao)
if raiz != False:
    print('Iterações: ' + str(dados[0]) + '\nRaiz: ' + str(raiz) + "\n|f(Raiz)|: " + str(dados[1]))