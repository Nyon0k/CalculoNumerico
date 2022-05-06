import math

def f(x):
    f = (x*math.log10(x))-1
    return f

a = 2
b = 3
tol = 1e-9
x = (a*f(b)-b*f(a))/(f(b)-f(a))

k = 0

while abs(f(x)) > tol:

    x = (a*f(b)-b*f(a))/(f(b)-f(a))

    print(k, a, x, b, f(a), f(x), f(b))

    if f(a)*f(x) < 0:
        a = a
        b = x
    elif f(x)*f(b) < 0:
        a = x
        b = b

    k += 1

print('O resultado é: ', x)