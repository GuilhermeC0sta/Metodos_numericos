'''from math import sin, cos, log, pi
import numpy as np
def bissecao(f, a, b, TOL):
  def ponto_medio(a, b):
    """Calcula o ponto médio do intervalo [a, b]."""
    return (a + b) / 2

  pontos = []
  x = ponto_medio(a, b)
  pontos.append(x)

  while abs(f(x)) > TOL:
    # Se f(a) e f(x) têm sinais diferentes, a raiz está na metade inferior do intervalo.
    if f(a) * f(x) < 0:
      b = x
    # Caso contrário, a raiz está na metade superior do intervalo.
    else:
      a = x

    # Calcula o novo ponto médio.
    x = ponto_medio(a, b)
    pontos.append(x)

  return pontos

def newton(f, df, x0, TOL):
  """
  Gera uma sequência de aproximações usando o método de Newton.

  Parâmetros:
    f: A função cuja raiz queremos encontrar.
    df: A derivada da função f.
    x0: Uma aproximação inicial da raiz.
    TOL: A tolerância de erro.

  Retorno:
    Uma lista de pontos que representam as aproximações sucessivas da raiz.
  """

  pontos = []
  x = x0
  pontos.append(x)

  while abs(f(x)) > TOL:
    # Calcula a próxima aproximação usando a fórmula de Newton.
    x = x - f(x) / df(x)
    pontos.append(x)

  return pontos

import matplotlib.pyplot as plt

def plot_aproximacoes(f, x_min, x_max, pontos_bissecao, pontos_newton):
  """
  Plota o gráfico de y = f(x) junto com as sequências de pontos de aproximação do método da bisseção e do método de Newton.

  Argumentos:
    f: A função a ser plotada.
    x_min: O valor mínimo de x.
    x_max: O valor máximo de x.
    pontos_bissecao: Uma lista de pontos (x, f(x)) do método da bisseção.
    pontos_newton: Uma lista de pontos (x, f(x)) do método de Newton.

  Retorna:
    None.
  """

  # Gera os pontos da função.
  x = np.linspace(x_min, x_max, 1000)
  y = f(x)

  # Plota o gráfico da função.
  plt.plot(x, y, label="f(x)")

  # Plota os pontos de aproximação do método da bisseção.
  plt.scatter([p[0] for p in pontos_bissecao], [p[1] for p in pontos_bissecao], label="Método da bisseção")

  # Plota os pontos de aproximação do método de Newton.
  plt.scatter([p[0] for p in pontos_newton], [p[1] for p in pontos_newton], label="Método de Newton")

  # Adiciona legendas e título.
  plt.legend()
  plt.title("Gráfico de f(x) com pontos de aproximação")

  # Mostra o gráfico.
  plt.show()


# Exemplo de uso.
def f1(x):
  return x - 2**(-x)

def f2(x):
  return x + 1 - 2 * sin(pi * x)

def f3(x):
  return 2 * x * cos(2 * x) - (x + 1)**2

def f4(x):
  return log(x) - 2**x + x**2

TOL = 1e-6

pontos = bissecao(f1, 0, 1, TOL)
#plot_pontos_aproximacao(f1, pontos)
pontos = bissecao(f2, 0, 0.5, TOL)
#plot_pontos_aproximacao(f2, pontos)
pontos = bissecao(f3, -3, -2, TOL)
#plot_pontos_aproximacao(f3, pontos)
pontos = bissecao(f4, 3, 5, TOL)
#plot_pontos_aproximacao(f4, pontos)













# Definindo a função f(x) = x^2 - 2
def f(x):
    return x**2 - 2

# Definindo o intervalo e a tolerância
p0 = 1
p1 = 2
TOL = 1e-5

approximations = bissecao(f, p0, p1, TOL)

print(approximations)
'''

from math import sin, cos, log, pi
import matplotlib.pyplot as plt
import numpy as np
def bissecao(f, a, b, tol, max_iter):
  x = []

  while abs(b - a) > tol and max_iter > 0:
    m = (a + b) / 2
    f_m = f(m)

    if f_m == 0:
      return x + [m]
    elif f_m > 0:
      b = m
    else:
      a = m
    x.append(m)
    max_iter -= 1
  return x

def newton(f, fprime, x0, tol, max_iter):
  x = []

  while abs(f(x0)) > tol and max_iter > 0:
    x.append(x0)
    x0 = x0 - f(x0) / fprime(x0)
    max_iter -= 1
  return x

def plot_aproximacoes(f, x, title):
  x_plot = np.linspace(min(x) - 1, max(x) + 1, 100)
  y_plot = f(x_plot)
  plt.plot(x_plot, y_plot, label="f(x)")

  for xi in x:
    plt.plot([xi, xi], [-1, 1], color="red", linestyle="dashed")

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
