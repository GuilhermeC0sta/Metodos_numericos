import matplotlib.pyplot as plt
import numpy as np

def approximate_root(f, p0, TOL, max_iterations=100):
    pn = p0
    pn_list = [pn]

    for n in range(1, max_iterations + 1):
        pn_prev = pn
        pn = f(pn_prev)

        pn_list.append(pn)

        if abs(pn - pn_prev) < TOL:
            break

    return pn_list

# Definindo a função f(x) = x^2 - 2
def f(x):
    return x**2 - 2

# Definindo o ponto inicial e a tolerância
p0 = 1.5
TOL = 1e-5

# Calculando a sequência de aproximações pn
approximations = approximate_root(f, p0, TOL)

# Criando o gráfico da função f(x)
x = np.linspace(0, 3, 100)  # Gerando valores de x para o gráfico
y = f(x)                    # Calculando os valores de y = f(x)

plt.plot(x, y, label='f(x) = x^2 - 2')  # Gráfico da função f(x)
plt.scatter(approximations, [f(p) for p in approximations], c=range(len(approximations)), cmap='viridis', label='Aproximações')  # Pontos da sequência de aproximações coloridos pelo índice
plt.colorbar(label='Índice')  # Adicionando uma barra de cor para representar o índice

plt.xlabel('x')             # Rótulo do eixo x
plt.ylabel('f(x)')          # Rótulo do eixo y
plt.title('Raiz de f(x)')   # Título do gráfico
plt.legend()                # Adicionando legenda

# Exibindo o gráfico
plt.show()
