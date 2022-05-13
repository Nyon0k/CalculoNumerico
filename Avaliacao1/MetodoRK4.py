import numpy as np

#função da EDO dada
def f(x, y):
    r = y*np.cos(x)
    return r

#metodo de Euler RK4
def rk4(x0, y0, h, qPassos):
    for _ in range(qPassos):
        k1 = f(x0, y0)
        k2 = f(x0+h/2, y0+k1*h/2)
        k3 = f(x0+h/2, y0+k2*h/2)
        k4 = f(x0+h, y0+k3*h)
        k = (k1+2*k2+2*k3+k4)/6
        y_atual = y0+k*h
        x0 = x0+h
        y0 = y_atual
    return y_atual

#Dados do PVI
intervalo = [0, 1]
x0, y0 = 0, 1
qPassos = 10
h = (intervalo[1]-intervalo[0])/qPassos
print('Raiz aproximada:', rk4(x0, y0, h, qPassos))