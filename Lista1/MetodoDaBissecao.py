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
def bissecao(a, b, err):
    if testeBolzano(a, b) == True:
        while math.fabs(b-a)/2 > err:
            x = (a+b)/2
            if func(x) == 0:
                print('Raiz: ', x)
                return x
            else:
                if testeBolzano(a, x) == True:
                    b = x
                else:
                    a = x
        print('Raiz aproximada: ', x)
        return
    else:
        print('Não há raiz nesse intervalo')
        return

##### variaveis pré-definidas #####
a, b = 2, 3 #intervalo [a,b]
err = 1e-7 #tolerancia do erro
raiz = bissecao(a, b, err)