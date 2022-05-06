import math as m
import numpy as np

def f(x):
  """
  Função definida para utilizarmos no cálculo de Newton-Raphson
  """
  return (x*m.log10(x))-1

def derivada(x):
  """
  Derivada da função f(x) = x² - 3x + 1
  """
  return m.log10(x)+1/np.log(10)

def newton_raphson(x, tolerancia, iteracao_max):
  """
  Método de Newton Raphson para encontrar raízes aproximadas
  """
  # Caso já seja encontrado a raíz de primeira para x, retorne-a diretamente.
  if m.fabs(f(x)) <= tolerancia:
    return x

  i = 0
  # Queremos que o nosso critério ao invés da diferença entre os pontos serem 
  # menor do que o erro, tomaremos a iteração máxima como a nossa 
  # forma de aproximação.
  while i <= iteracao_max:
    x1 = x - (f(x) / derivada(x))
    if m.fabs(f(x1)) <= tolerancia:
      return x1
    x = x1
    i += 1
  
  raise ValueError("Número máx. de iterações atingido")

print(newton_raphson(2, 1e-7, 100))