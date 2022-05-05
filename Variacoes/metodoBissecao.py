import math

#Executa o cálculo da função de entrada
def func(x):
    func_result = (x*math.log10(x))-1
    return func_result

#Teste de Bolzano
def testeBolzano(x, y):
    if func(x)*func(y) < 0:
        return True
    else:
        return False

#Executa o método da bisseção
def bissecao(a, b, x_inicial, err):
    while True:
        x = (a+b)/2
        if testeBolzano(a, x) == True:
            b = x
        else:
            a = x
        if b-a <= err:
            return x
        if abs(func(x)) <= err:
            return x

##### variaveis pré-definidas #####
a, b = 2, 3 #intervalo [a,b]
err = 1e-8 #tolerancia do erro
x_inicial = 2
print(bissecao(a, b, x_inicial, err))