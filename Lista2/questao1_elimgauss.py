import numpy as np

def eliminacao_gaussiana(A, b):
    n = len(b)
    
    # Concatenando a matriz A com o vetor b para formar a matriz aumentada
    matriz_aumentada = np.hstack((A, b.reshape(-1, 1)))
    
    # Eliminação por etapas
    for i in range(n):
        # Pivô é o elemento diagonal atual
        pivot = matriz_aumentada[i, i]
        
        # Normalizando a linha atual (dividindo pelo pivô)
        matriz_aumentada[i, :] /= pivot
        
        # Eliminando elementos abaixo do pivô
        for j in range(i + 1, n):
            fator = matriz_aumentada[j, i]
            matriz_aumentada[j, :] -= fator * matriz_aumentada[i, :]
    
    # Resolvendo o sistema triangular superior por substituição regressiva
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = matriz_aumentada[i, -1] - np.dot(matriz_aumentada[i, i+1:n], x[i+1:])
    
    return x

# Exemplo de sistema linear
A = np.array([[2, 3, -1],
              [1, -2, 4],
              [3, 1, 2]], dtype=float)
b = np.array([7, 1, 5], dtype=float)
'''
A = np.array([[4, -1, 2],
              [2, 3, -1]
              [1, 2, 3]])
b = np.array([10, 5, 8])
'''
'''
A = np.array([[1, 2, -1],
              [3, -1, 4]
              [2, 3, 2]])
b = np.array([3, 8, 7])
'''
# Resolvendo o sistema
solucao = eliminacao_gaussiana(A, b)
print("Solução:")
for i, valor in enumerate(solucao):
    print(f"x{i+1} = {valor:.4f}")
