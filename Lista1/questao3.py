def calcular_intervalo(p):
  erro_relativo_maximo = 10**(-2)
  valor_minimo = p * (1 - erro_relativo_maximo)
  valor_maximo = p * (1 + erro_relativo_maximo)
  print(f'p = {p}')
  print(f'Intervalo: [{valor_minimo:.2f}, {valor_maximo:.2f}]\n')


calcular_intervalo(150)
calcular_intervalo(900)
calcular_intervalo(1500)
calcular_intervalo(90)
