import matplotlib.pyplot as plt

def plot_grafico(f, a, b, delta):
  x = [a + i * delta for i in range(int((b - a) / delta) + 1)]

  # Calcula os valores de f(x) para cada ponto na lista.
  y = [f(xi) for xi in x]

  plt.plot(x, y, '-')
  plt.xlabel('x')
  plt.ylabel('y')
  plt.show()

def f(x):
  return x**2

plot_grafico(f, -2, 2, 0.1)
