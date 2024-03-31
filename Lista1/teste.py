'''# Define the exact values
from decimal import Decimal
exact_result_a = Decimal((121 - 0.327) - 119)
exact_result_b = Decimal((121 - 119) - 0.327)

# Perform the calculations using three-digit rounding arithmetic
rounded_result_a = round(exact_result_a, 3)
rounded_result_b = round(exact_result_b, 3)

# Compute the absolute errors
absolute_error_a = abs(rounded_result_a - exact_result_a)
absolute_error_b = abs(rounded_result_b - exact_result_b)

# Compute the relative errors
relative_error_a = (absolute_error_a / exact_result_a) * 100
relative_error_b = (absolute_error_b / exact_result_b) * 100

# Output the results
print(f"a) Rounded result: {rounded_result_a}, Absolute error: {absolute_error_a}, Relative error: {relative_error_a}%")
print(f"b) Rounded result: {rounded_result_b}, Absolute error: {absolute_error_b}, Relative error: {relative_error_b}%")
'''

def calcular_intervalo(p, erro_relativo_maximo):
  """
  Calcula o maior intervalo no qual p pode estar para um determinado erro relativo máximo.

  Argumentos:
    p: O valor aproximado.
    erro_relativo_maximo: O erro relativo máximo.

  Retorno:
    Uma tupla contendo o valor mínimo e o valor máximo do intervalo.
  """

'''
  valor_minimo = p * (1 - erro_relativo_maximo)
  valor_maximo = p * (1 + erro_relativo_maximo)
  return valor_minimo, valor_maximo

# Exemplo de uso
p = 150
erro_relativo_maximo = 10**(-2)

valor_minimo, valor_maximo = calcular_intervalo(p, erro_relativo_maximo)

print(f"Intervalo: [{valor_minimo:.2f}, {valor_maximo:.2f}]")
'''
'''
def bhaskara(a, b, c):
  delta = b**2 - 4 * a * c

  # Condições para o tipo de solução
  if delta > 0:
    # Duas raízes reais distintas
    x1 = (-b + (delta**0.5)) / (2 * a)
    x2 = (-b - (delta**0.5)) / (2 * a)
    return [x1, x2]
  elif delta == 0:
    # Uma raiz real dupla
    x = -b / (2 * a)
    return [x]
  else:
    # Sem raízes reais
    return None
  

def formula_alternativa(a, b, c):
    delta = b**2 - 4 * a * c

    x1 = ((-2 * c) / (b + (delta**0.5)))
    x2 = ((-2 * c) / (b - (delta**0.5)))
    
    return x1, x2, relativo


# Exemplo de uso
a = 1
b = 2
c = 3

raizes = bhaskara(a, b, c)
raiz1, raiz2, relativo = formula_alternativa(a, b, c)


if raizes is not None:
  print(f"Raízes: {raizes}")
else:
  print("Sem raízes reais")
'''

#def log2(x):
"""
  Calcula o logaritmo de base 2 de um número.

  Args:
    x: O número para calcular o logaritmo.

  Returns:
    O logaritmo de base 2 de x.
  """
'''
def log2(x):
    if x <= 0:
        raise ValueError("O argumento de log2 deve ser maior que 0.")
    result = 0.0
    y = x
    if x < 1:
        while y < 1:
            result -= 1
            y *= 2
    elif x >= 2:
        while y >= 2:
            result += 1
            y /= 2
    z = (y - 1) / (y + 1)
    term = z
    n = 1
    while abs(term) > 1e-15:
   9     result += term
        n += 2
        term = (z ** n) / n
    return result
'''
'''
import matplotlib.pyplot as plt

def graph_f(f, a, b, delta):
    x = a
    xs = []
    ys = []

    while x <= b:
        xs.append(x)
        ys.append(f(x))
        x += delta

    plt.plot(xs, ys)
    plt.show()

graph_f(lambda x: x**2 + 1, -5, 5, 0.5)
'''

'''
x = 1.1102230246251565e-16

# Calcula o logaritmo de base 2 de 0.1
log2_result = log2(x)

# Imprime o resultado
print(f"log2({x}) = {log2_result}")
'''
'''
def bissecao(f, a, b, TOL):
    p = (a + b) / 2
    pn = [p]

    while abs(f(p)) > TOL:
        if f(a) * f(p) < 0:
            b = p

        else:
            a = p

        p = (a + b) / 2
        pn.append(p)

    return pn

def f(x):
    return x**2 - 2

a = 0
b = 2
TOL = 1e-6

raiz_bissecao = bissecao(f, a, b, TOL)
print(raiz_bissecao)
'''
'''
import matplotlib.pyplot as plt

def plot_funcao(f, a, b, delta):
    x = a
    xs = []
    ys = []

    while x <= b:
        xs.append(x)
        ys.append(f(x))
        x += delta

    plt.plot(xs, ys, label='f(x)')

def df(x):
    return 2*x

def plot_bissecao(f, a, b, tol_bissec):
    a_bissec, b_bissec = a, b
    seq_bissec = []

    while (b_bissec - a_bissec) / 2 > tol_bissec:
        c_bissec = (a_bissec + b_bissec) / 2
        seq_bissec.append((c_bissec, f(c_bissec)))

        if f(a_bissec) * f(c_bissec) < 0:
            b_bissec = c_bissec
        else:
            a_bissec = c_bissec

    plt.plot(*zip(*seq_bissec), marker='o', linestyle='-', color='red', label='Bisseção Points')

def plot_newton(f, df, x0, tol_newton):
    seq_newton = [(x0, f(x0))]

    while abs(f(x0)) > tol_newton:
        x0 = x0 - f(x0) / df(x0)
        seq_newton.append((x0, f(x0)))

    plt.plot(*zip(*seq_newton), marker='o', linestyle='-', color='blue', label='Newton Points')

plt.figure(figsize=(15, 5))

# Bisseção e Newton
plt.subplot(1, 3, 1)
plot_funcao(lambda x: x**2 - 2, 0, 2, 0.1)
plot_bissecao(lambda x: x**2 - 2, 0, 2, 1e-6)
plot_newton(lambda x: x**2 - 2, df, 1, 1e-6)
plt.title('Ambos os métodos')

# Bisseção
plt.subplot(1, 3, 2)
plot_funcao(lambda x: x**2 - 2, 0, 2, 0.1)
plot_bissecao(lambda x: x**2 - 2, 0, 2, 1e-6)
plt.title('Método da Bisseção')

# Newton
plt.subplot(1, 3, 3)
plot_funcao(lambda x: x**2 - 2, 0, 2, 0.1)
plot_newton(lambda x: x**2 - 2, df, 1, 1e-6)
plt.title('Método de Newton')

plt.tight_layout()
plt.show()
'''
'''
from math import sin, cos, pi, log
import matplotlib.pyplot as plt

def newton_approx(f, df, x0, tol):
    prev = 1e+100
    curr = x0
    f_c = f(curr)

    xs = [curr]
    ys = [f_c]

    while abs(curr - prev) > tol:
        prev = curr
        curr = curr - f(curr) / df(curr)
        f_c = f(curr)

        xs.append(curr)
        ys.append(f_c)

    return xs, ys

def bisection_approx(f, a, b, tol):
    prev = 1e+100
    curr = (a + b) / 2
    f_c = f(curr)

    xs = [curr]
    ys = [f_c]
    while abs(curr - prev) > tol:
        if f(a) * f_c < 0:
            b = curr
        else:
            a = curr

        prev = curr
        curr = (a + b) / 2
        f_c = f(curr)

        xs.append(curr)
        ys.append(f_c)
    
    return xs, ys

def plot_funcao(f, a, b, delta):
    x = a
    xs = []
    ys = []

    while x <= b:
        xs.append(x)
        ys.append(f(x))
        x += delta

    plt.plot(xs, ys, label='f(x)')

def plot_bissecao(f, a, b, tol):
    approx = bisection_approx(f, a, b, tol)
    plt.plot(approx[0], approx[1], marker='o', linestyle='-', color='red', label='Bisseção Points')

def plot_newton(f, df, x0, tol):
    approx = newton_approx(f, df, x0, tol)
    plt.plot(approx[0], approx[1], marker='o', linestyle='-', color='blue', label='Newton Points')

def plot_tudo(function, derivative, lower, upper, x0):
    plt.figure(figsize=(15, 5))
    plt.subplot(1, 3, 1)
    plot_funcao(function, lower, upper, 0.05)
    plot_bissecao(function, lower, upper, 1e-6)
    plot_newton(function, derivative, x0, 1e-6)
    plt.title('Ambos os métodos')

    # Bisseção
    plt.subplot(1, 3, 2)
    plot_funcao(function, lower, upper, 0.05)
    plot_bissecao(function, lower, upper, 1e-6)
    plt.title('Método da Bisseção')

    # Newton
    plt.subplot(1, 3, 3)
    plot_funcao(function, lower, upper, 0.05)
    plot_newton(function, derivative, x0, 1e-6)
    plt.title('Método de Newton')

    plt.tight_layout()
    plt.show()

a = lambda x: x - 2 ** (-x)
dfa = lambda x: log(2) * 2 ** (-x) + 1
xa = 0.5
la = 0
ua = 1

b = lambda x: x + 1 - 2*sin(pi*x)
dfb = lambda x: 1 - 2*pi*cos(pi*x)
xb = 0.25
lb = 0
ub = 0.5

c = lambda x: 2*x*cos(2*x) - (x + 1) ** 2
dfc = lambda x: -2*(1 + x - cos(2*x) + 2*x*sin(2*x))
xc = -2.5
lc = -3
uc = -2

d = lambda x: log(x) - 2 ** x + x ** 2
dfd = lambda x: 1/x + 2*x - log(2) * 2 ** x
xd = 4
ld = 3
ud = 5

for function, derivative, lower, upper, x0 in [(a, dfa, la, ua, xa), (b, dfb, lb, ub, xb), (c, dfc, lc, uc, xc), (d, dfd, ld, ud, xd)]:
    plot_tudo(function, derivative, lower, upper, x0)
'''

from math import sin, cos, log, pi
import matplotlib.pyplot as plt
import numpy as np
def bissecao(f, a, b, tol, max_iter):
  x = []

  # Condição de parada
  while abs(b - a) > tol and max_iter > 0:
    # Ponto médio do intervalo
    m = (a + b) / 2

    # Avaliação da função no ponto médio
    f_m = f(m)

    # Se f(m) for zero, a raiz foi encontrada
    if f_m == 0:
      return x + [m]

    # Se f(m) for positivo, a raiz está no intervalo [a, m]
    elif f_m > 0:
      b = m

    # Se f(m) for negativo, a raiz está no intervalo [m, b]
    else:
      a = m

    # Armazenar a aproximação atual
    x.append(m)

    # Diminuir o número máximo de iterações
    max_iter -= 1

  # Retornar a lista de aproximações
  return x

def newton(f, fprime, x0, tol, max_iter):
  x = []

  # Condição de parada
  while abs(f(x0)) > tol and max_iter > 0:
    # Aproximação atual da raiz
    x.append(x0)

    # Cálculo da próxima aproximação
    x0 = x0 - f(x0) / fprime(x0)

    # Diminuir o número máximo de iterações
    max_iter -= 1

  # Retornar a lista de aproximações
  return x

def plot_aproximacoes(f, x, title):
  x_plot = np.linspace(min(x) - 1, max(x) + 1, 100)
  y_plot = f(x_plot)

  # Plotando a função
  plt.plot(x_plot, y_plot, label="f(x)")

  # Plotando as aproximações
  for xi in x:
    plt.plot([xi, xi], [-1, 1], color="red", linestyle="dashed")

  # Adicionando título e legendas
  plt.title(title)
  plt.legend()
  plt.show()



def f(x):
  return x - 2**(-x)

def fprime(x):
  return 1 + log(2) * 2**(-x)

def f1(x):
  return x + 1 - 2 * np.sin(np.pi * x)

def f1prime(x):
  return 1 - 2 * np.pi * np.cos(np.pi * x)

def f2(x):
  return 2 * x * np.cos(2 * x) - (x + 1)**2

def f2prime(x):
  return -2 * x + 2 * (-2 * x * np.sin(2 *x)+np.cos(2 * x)) - 2

def f3(x):
  return np.log(x) - 2**x + x**2

def f3prime(x):
  return 1/x - 2**x * log(2) + 2*x

tol = 1e-5
max_iter = 100

x = bissecao(f, 0, 1, tol, max_iter)
y = newton(f, fprime, 0, tol, max_iter)
x1 = bissecao(f1, 0, 0.5, tol, max_iter)
y1 = newton(f1, f1prime, 0, tol, max_iter)
x2 = bissecao(f2, -3, -2, tol, max_iter)
y2 = newton(f2, f2prime, -3, tol, max_iter)
x3 = bissecao(f3, 3, 5, tol, max_iter)
y3 = newton(f3, f3prime, 3, tol, max_iter)

plot_aproximacoes(f, x, "Bisseção")
plot_aproximacoes(f, y, "Newton")
plot_aproximacoes(f1, x1, "Bisseção")
plot_aproximacoes(f1, y1, "Newton")
plot_aproximacoes(f2, x2, "Bisseção")
plot_aproximacoes(f2, y2, "Newton")
plot_aproximacoes(f3, x3, "Bisseção")
plot_aproximacoes(f3, y3, "Newton")
