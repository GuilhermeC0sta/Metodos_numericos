def f(x):
  return x**2 - 1

def bissecao(f, a, b, tolerancia):
  while abs(b - a) > tolerancia:
    m = (a + b) / 2
    if f(m) == 0:
      return m
    elif f(m) * f(a) < 0:
      b = m
    else:
      a = m
  return (a + b) / 2

def newton(f, df, x0, tolerancia):
  while abs(f(x0)) > tolerancia:
    x0 = x0 - f(x0) / df(x0)
  return x0


funcao = f
a = -1
b = 1
tolerancia = 1e-5

# Resolução usando o método da bisseção
raiz_bissecao = bissecao(funcao, a, b, tolerancia)
print(f"Raiz pela bisseção: {raiz_bissecao}")

# Resolução usando o método de Newton
df = lambda x: 2*x
raiz_newton = newton(funcao, df, 0.5, tolerancia)
print(f"Raiz pelo método de Newton: {raiz_newton}")

