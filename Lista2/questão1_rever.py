import numpy as np

def substituicao_reversa(A, b):
  """
  Função para resolver Ax = b usando o método de substituição reversa.

  Argumentos:
    A: Matriz numpy de coeficientes (n x n).
    b: Vetor numpy de termos independentes (n x 1).

  Retorno:
    x: Vetor numpy de soluções (n x 1).
  """

  n = len(A)
  x = np.zeros(n)

  # Começando pela última equação
  for i in range(n-1, -1, -1):
    # Substituindo valores nas equações anteriores
    soma = 0
    for j in range(i+1, n):
      soma += A[i][j] * x[j]

    # Calculando a solução para a variável x_i
    x[i] = (b[i] - soma) / A[i][i]

  return x

# Exemplo de uso
A = np.array([[2, 3, -1],
              [1, -2, 4],
              [3, 1, 2]], dtype=float)
b = np.array([7, 1, 5], dtype=float)

x = substituicao_reversa(A, b)

print("Solução:", x)
