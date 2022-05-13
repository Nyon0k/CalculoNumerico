import numpy as np

#função da EDO dada
def f(x, y):
    r = y*np.cos(x)
    return r

#metodo de Euler RK2
def rk2(x0, y0, h, qPassos):
    for _ in range(qPassos):
        k1 = f(x0, y0)
        k2 = f(x0+h/2, y0+k1*h/2)
        k2 = f(x0+h, y0+k1*h)
        y_atual = y0+(1/2)*(k1+k2)*h
        x0 = x0+h
        y0 = y_atual
    return y_atual

#Dados do PVI
intervalo = [0, 1]
x0, y0 = 0, 1
qPassos = 10
h = (intervalo[1]-intervalo[0])/qPassos
print('Raiz aproximada:', rk2(x0, y0, h, qPassos))

