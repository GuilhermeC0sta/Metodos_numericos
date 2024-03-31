from math import sin, cos, log, pi
def f1(x):
  return x - 2**(-x)

def f2(x):
  return x + 1 - 2 * sin(pi * x)

def f3(x):
  return 2 * x * cos(2 * x) - (x + 1)**2

def f4(x):
  return log(x) - 2**x + x**2

def bissecao(a, b, epsilon, f):
  n = 0
  while abs(b - a) > epsilon:
    m = (a + b) / 2
    if f(m) == 0:
      return m
    elif f(m) < 0:
      b = m
    else:
      a = m
    n += 1
  return (a + b) / 2, n

epsilon = 1e-4

raiz1, n1 = bissecao(0, 1, epsilon, f1)
raiz2, n2 = bissecao(0, 0.5, epsilon, f2)
raiz3, n3 = bissecao(-3, -2, epsilon, f3)
raiz4, n4 = bissecao(3, 5, epsilon, f4)

print(f"Raiz da equação A: {raiz1}")
print(f"Número de iterações: {n1}")
print(f"Raiz da equação B: {raiz2}")
print(f"Número de iterações: {n2}")
print(f"Raiz da equação C: {raiz3}")
print(f"Número de iterações: {n3}")
print(f"Raiz da equação D: {raiz4}")
print(f"Número de iterações: {n4}")