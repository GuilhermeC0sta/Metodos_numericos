import numpy as np

def decomposicao_ptlu(A, b):
  """
  Função para realizar a decomposição PtLU de uma matriz A e resolver o sistema Ax = b.

  Argumentos:
    A: Matriz numpy de coeficientes (n x n).
    b: Vetor numpy de termos independentes (n x 1).

  Retorno:
    x: Vetor numpy de soluções (n x 1).
    P: Matriz numpy de permutação (n x n).
  """

  n = A.shape[0]  # Tamanho da matriz A
  L = np.eye(n)  # Inicializa a matriz L como a matriz identidade
  U = A.copy()  # Inicializa a matriz U como uma cópia de A
  P = np.eye(n)  # Inicializa a matriz de permutação P como a matriz identidade

  for k in range(n):
    # Encontra o pivô (elemento máximo em valor absoluto na coluna k)
    pivot_row = np.argmax(np.abs(U[k:, k])) + k

    # Troca as linhas k e pivot_row em U e P
    U[[k, pivot_row], :] = U[[pivot_row, k], :]
    P[[k, pivot_row], :] = P[[pivot_row, k], :]

    # Atualiza a matriz L com os multiplicadores
    L[k+1:, k] = U[k+1:, k] / U[k, k]

    # Atualiza a matriz U
    U[k+1:, k:] -= L[k+1:, k:k+1] @ U[k:k+1, k:]

  # Resolvendo o sistema triangular inferior Ly = Pb
  y = np.linalg.solve(L, P @ b)

  # Resolvendo o sistema triangular superior Ux = y
  x = np.linalg.solve(U, y)

  return x, P

# Exemplo de matriz A e vetor b
A = np.array([[2, 3, -1],
              [1, -2, 4],
              [3, 1, 2]], dtype=float)
b = np.array([7, 1, 5], dtype=float)

# Calcula a decomposição PtLU e encontra os valores de x e P
solucao, P = decomposicao_ptlu(A, b)

# Exibe a solução
print("Solução:")
for i, valor in enumerate(solucao):
  print(f"x{i+1} = {valor:.4f}")

# Exibe a matriz de permutação P
print("Matriz de Permutação P:")
print(P)
