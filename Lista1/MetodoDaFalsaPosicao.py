import math

dados = [] #salvar iterações e |f(Raiz)|

#Executa o cálculo da função de entrada
def f(x):
    f_result = x*math.log10(x)-1
    return f_result

#Teste de Bolzano
def testeBolzano(x, y):
    if f(x)*f(y) < 0:
        return True
    else:
        return False

#Executa o método da bisseção
def falsaPosicao(a, b, err):
    if testeBolzano(a, b) == True:
        cont = 0
        while True:
            cont += 1
            aprox = (a*f(b)-b*f(a))/(f(b)-f(a))
            if abs(f(aprox)) < err:
                dados.append(cont)
                dados.append(abs(f(aprox)))
                return aprox
            else:
                if testeBolzano(a, aprox) == True:
                    b = aprox
                else:
                    a = aprox
    else:
        print('Não há raiz nesse intervalo')
        return

##### variaveis pré-definidas #####
a, b = 2, 3 #intervalo [a,b]
err = 1e-7 #tolerancia do erro
raiz = falsaPosicao(a, b, err)
print('Iterações: ' + str(dados[0]) + '\nRaiz: ' + str(raiz) + "\n|f(Raiz)|: " + str(dados[1]))