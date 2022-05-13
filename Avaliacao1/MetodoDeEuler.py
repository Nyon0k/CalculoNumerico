#função da EDO dada
def f(x, y):
    r = y - x
    return r

#metodo de Euler
def euler(x0, y0, h, qPassos):
    for i in range(qPassos):
        y_atual = y0+h*f(x0, y0)
        y0 = y_atual
        x0 = x0+h
    return y_atual

#Dados do PVI
intervalo = [0, 1]
x0, y0 = 0, 2
qPassos = 4
h = (intervalo[1]-intervalo[0])/qPassos
print('Raiz aproximada:', euler(x0, y0, h, qPassos))

