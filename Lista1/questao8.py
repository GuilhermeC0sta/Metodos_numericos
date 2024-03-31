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

# Definindo a função f(x) = x^2 - 2
def f(x):
    return x**2 - 2

# Definindo o intervalo e a tolerância
p0 = 1
p1 = 2
TOL = 1e-5

approximations = bissecao(f, p0, p1, TOL)

print(approximations)
