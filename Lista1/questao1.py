#numtest = '0b010000000011101110010001000000000000000000000000000000000000000'

def rep_ponto_flutuante(numtest):
  array = list(numtest[2:])

  a = list(map(int, array)) #converte pra inteiros

  s = a[:1][0] #[0] faz com que se pegue o primeiro elemento do slice, isso faz s ter um valor e nao ser um array

  carac = 11
  c = 0
  f = 0
  mantissa = 12

  for i in range(1, 12):
    carac = carac - 1
    c = c + a[i] * (2**carac)
    
  e = 2**(c - 1023)
  f_array = a[12:]

  for j in range(0, 51):
    if(f_array[j] == 1):
      f = f + 1 * (1/2)**(j + 1)

  resultado = (-1)**s * e * (1 + f)
  print(resultado)

rep_ponto_flutuante('0b0100000010101001001100000000000000001000000000001000000001000000') #a
rep_ponto_flutuante('0b1100000010101011001100000000001000000000000010000000000000000000') #b
rep_ponto_flutuante('0b0011010111110001001100000000000000100000000000000000000001000000') #c
rep_ponto_flutuante('0b1010111110110101001100000000000000000000000001000000001000000001') #d
