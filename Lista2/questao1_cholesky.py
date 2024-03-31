def eh_simetrica(A):
  """
  Verifica se a matriz A é simétrica.

  Argumentos:
    A: Matriz a ser verificada.

  Retorno:
    True se a matriz for simétrica, False caso contrário.
  """
  n = len(A)
  for i in range(n):
    for j in range(i + 1, n):
      if A[i][j] != A[j][i]:
        return False
  return True

def cholesky(A):
  """
  Realiza a decomposição de Cholesky da matriz A.

  Argumentos:
    A: Matriz a ser decomposta.

  Retorno:
    L: Matriz triangular inferior L, tal que L * L^T = A.
  """
  n = len(A)
  L = [[0 for _ in range(n)] for _ in range(n)]
  for i in range(n):
    for j in range(i + 1):
      s = 0
      for k in range(j):
        s += L[i][k] * L[j][k]
      if i == j:
        L[i][i] = (A[i][i] - s)**0.5
      else:
        L[i][j] = (A[i][j] - s) / L[j][j]
  return L

def resolver_cholesky(A, b):
  """
  Resolve o sistema Ax = b usando a decomposição de Cholesky.

  Argumentos:
    A: Matriz A do sistema.
    b: Vetor b do sistema.

  Retorno:
    x: Solução do sistema Ax = b.
  """
  n = len(A)
  # Verifica se a matriz é simétrica
  if not eh_simetrica(A):
    raise ValueError("A matriz A não é simétrica.")

  # Realiza a decomposição de Cholesky
  L = cholesky(A)

  # Resolve o sistema L * y = b
  y = [0 for _ in range(n)]
  for i in range(n):
    s = 0
    for k in range(i):
      s += L[i][k] * y[k]
    y[i] = (b[i] - s) / L[i][i]

  # Resolve o sistema L^T * x = y
  x = [0 for _ in range(n)]
  for i in range(n - 1, -1, -1):
    s = 0
    for k in range(i + 1, n):
      s += L[k][i] * x[k]
    x[i] = (y[i] - s) / L[i][i]

  return x

'''
A = [[2, 3, -1],
    [1, -2, 4],
    [3, 1, 2]]
b = [7, 1, 5]
'''
A = [[4, 1, 1],
    [1, 4.25, 1.5],
    [1, 1.5, 3.5]]
b = [1, 2, 3]

try:
  x = resolver_cholesky(A, b)
  print("Solução:", x)
except ValueError as e:
  print(e)
