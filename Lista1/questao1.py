numtest = '0b010000000011101110010001000000000000000000000000000000000000000'
#numero_str = input("Digite um número: ")
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