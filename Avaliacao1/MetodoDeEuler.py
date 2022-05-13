import math

#função da EDO dada
def fL1(L1, L2, t):
    r = -0.4427*math.sqrt(L1)+0.23*(4+4*math.sin(t))
    return r

def fL2(L1, L2, t):
    r = -0.4427*math.sqrt(L2)+0.4427*math.sqrt(L1)
    return r

#metodo de Euler Sistema
def eulerSistema(t, h, qPassos, L10, L20):
    L1 = L10
    L2 = L20
    for i in range(qPassos):
        kL1 = fL1(L1, L2, t)
        print('kL1', i, kL1)
        kL2 = fL2(L1, L2, t)
        print('kL2', i, kL2)
        L1_atual = L1+kL1*h
        L2_atual = L2+kL2*h
        L1 = L1_atual
        L2 = L2_atual
        t += h
    dados.append(t)
    dados.append(L1)
    dados.append(L2)
    return dados

#Dados do PVI
dados = []
intervalo = [0, 30]
# x0, y0 = 0, 2
t, L10, L20 = 0, 0, 0
qPassos = 2
# h = (intervalo[1]-intervalo[0])/qPassos
h = 1
dados = []
print('Raiz aproximada:', eulerSistema(t, h, qPassos, L10, L20))

