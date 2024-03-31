from decimal import Decimal

#n = (121 - 119) - 0.327 #d
#n = (121 - 0.327) - 119 #c
#n = (2/9) * (9/7) #g
#n = 133 + 0.921 #a
n = 133 - 0.499 #b
#n = 12.3456789
#n = ((13/14) - (6/7)) / ((2 * 2.718281828459045) - 5.4)
#n = (0.92857142857142857142857142857143 - 0.85714285714285714285714285714286) / 0.03656365691809

# Conta o numero de algarismos na parte inteira
def contar_algarismos_inteiros(num):
    # Convertendo o número para uma string e removendo o ponto decimal (se houver)
    num_str = str(num)

    # Verificando se o número inteiro é 0
    if num_str.split('.')[0] == '0':
        return 0
    else:
        return len(num_str.split('.')[0])

# Resolve o caso de 133.0
def imprimir_numero(num):
    if num == int(num):
        return(int(num))
    else:
        return(num)

def truncamento_3_digitos(n):
    num_int = contar_algarismos_inteiros(n) #10³, somente o expoente, sem o 10
    
    n_string = str(n / 10**num_int) # 0.133921
    n_string = n_string[0] + n_string[1] + n_string[2] + n_string[3] + n_string[4] # pega os 3 digitos

    trunc3 = Decimal(float(n_string) * 10**num_int) 

    n_string = str(trunc3)
    if n_string[0] == '0':
        n_string = n_string[0] + n_string[1] + n_string[2] + n_string[3] + n_string[4]
    elif len(n_string) > 4:
        n_string = n_string[0] + n_string[1] + n_string[2] + n_string[3] # pega os 3 digitos dnv

    trunc3digit = float(n_string)
    print(f'Truncamento de 3 digitos: {imprimir_numero(trunc3digit)}')
    erros(n, trunc3digit)

def truncamento_4_digitos(n):
    num_int = contar_algarismos_inteiros(n) 
    #print(num_int)
    n_string = str(n / 10**num_int) 
    n_string = n_string[0] + n_string[1] + n_string[2] + n_string[3] + n_string[4] + n_string[5]

    trunc4 = Decimal(float(n_string) * 10**num_int)

    n_string = str(trunc4)
    if n_string[0] == '0':
        n_string = n_string[0] + n_string[1] + n_string[2] + n_string[3] + n_string[4] + n_string[5]
    elif len(n_string) > 5:
        n_string = n_string[0] + n_string[1] + n_string[2] + n_string[3] + n_string[4]

    trunc4digit = float(n_string)

    print(f'Truncamento de 4 digitos: {imprimir_numero(trunc4digit)}')
    erros(n, trunc4digit)


def arredondamento_3_digitos(n):
    num_int = contar_algarismos_inteiros(n) 
    #print(num_int)
    n_string = str(n / 10**num_int)

    n_string = n_string[0] + n_string[1] + n_string[2] + n_string[3] + n_string[4] + n_string[5]
    if int(n_string[5]) >= 5:
        n_string = n_string[0] + n_string[1] + n_string[2] + n_string[3] + str(int(n_string[4]) + 1)
    else:
       n_string = n_string[0] + n_string[1] + n_string[2] + n_string[3] + n_string[4] 
    
    arredon3 = Decimal(float(n_string) * 10**num_int)
    
    n_string = str(arredon3)
    if n_string[0] == '0':
        if int(n_string[5]) >= 5:
            n_string = n_string[0] + n_string[1] + n_string[2] + n_string[3] + str(int(n_string[4]) + 1)
        else:
            n_string = n_string[0] + n_string[1] + n_string[2] + n_string[3] + n_string[4]
    elif len(n_string) > 4:
        if int(n_string[5]) >= 5:
            n_string = n_string[0] + n_string[1] + n_string[2] + str(int(n_string[3]) + 1)
        else:
            n_string = n_string[0] + n_string[1] + n_string[2] + n_string[3]

    arredon3digit = float(n_string)

    print(f'Arredondamento de 3 digitos: {imprimir_numero(arredon3digit)}')
    erros(n, arredon3digit)


def arredondamento_4_digitos(n):
    num_int = contar_algarismos_inteiros(n) 
    #print(num_int)
    n_string = str(n / 10**num_int)

    if len(n_string) >= 7:
        n_string = n_string[0] + n_string[1] + n_string[2] + n_string[3] + n_string[4] + n_string[5] + n_string[6]
        if int(n_string[6]) >= 5:
            n_string = n_string[0] + n_string[1] + n_string[2] + n_string[3] + n_string[4] + str(int(n_string[5]) + 1)
        else:
            n_string = n_string[0] + n_string[1] + n_string[2] + n_string[3] + n_string[4] + n_string[5]
    else:
        # Trata o caso em que o comprimento de n_string é menor do que 7
        n_string = n_string[:7]
    
    arredon4 = Decimal(float(n_string) * 10**num_int)
    
    n_string = str(arredon4)
    if n_string[0] == '0':
        if int(n_string[6]) >= 5:
            n_string = n_string[0] + n_string[1] + n_string[2] + n_string[3] + n_string[4] + str(int(n_string[5]) + 1)
        else:
            n_string = n_string[0] + n_string[1] + n_string[2] + n_string[3] + n_string[4] + n_string[5]
    elif len(n_string) > 5:
        if int(n_string[6]) >= 5:
            n_string = n_string[0] + n_string[1] + n_string[2] + n_string[3] + str(int(n_string[4]) + 1)
        else:
            n_string = n_string[0] + n_string[1] + n_string[2] + n_string[3] + n_string[4]

    arredon4digit = float(n_string)

    print(f'Arredondamento de 4 digitos: {imprimir_numero(arredon4digit)}')
    erros(n, arredon4digit)


def erros(p, pl):
    erro_absoluto = abs(p - pl)
    erro_relativo = erro_absoluto / abs(p)

    print("Erro Absoluto: ", erro_absoluto)
    print("Erro Relativo: ", erro_relativo)

def chamada(n):
  print("\n")
  print(f'Para {n}\n')
  truncamento_3_digitos(n)
  print("---------------------------------------------------")
  truncamento_4_digitos(n)
  print("---------------------------------------------------")
  arredondamento_3_digitos(n)
  print("---------------------------------------------------")
  arredondamento_4_digitos(n)
  print("---------------------------------------------------")
  print("\n")
  
def bhaskara(a, b, c):
  delta = b**2 - 4 * a * c

  x1 = (-b + (delta**0.5)) / (2 * a)
  x2 = (-b - (delta**0.5)) / (2 * a)

  real1 = Decimal(a) 
  real2 = Decimal(b)
  real3 = Decimal(c)
  real5 = (Decimal(-b) - Decimal((delta**0.5))) / Decimal((2 * a)) #aproximacao p*

  erro_absoluto = abs(x2 - float(real5))
  erro_relativo = erro_absoluto / abs(x2)

  return x1, x2, erro_relativo
'''
  if delta > 0:
    x1 = (-b + (delta**0.5)) / (2 * a)
    x2 = (-b - (delta**0.5)) / (2 * a)
    return x1, x2
  elif delta == 0:
    x = -b / (2 * a)
    return x
  else:
    return None
'''
def formula_alternativa(a, b, c):
    delta = b**2 - 4 * a * c

    x1 = ((-2 * c) / (b + (delta**0.5)))
    x2 = ((-2 * c) / (b - (delta**0.5)))

    real1 = Decimal(a) 
    real2 = Decimal(b)
    real3 = Decimal(c)
    real5 = (Decimal((-2 * c)) / (Decimal(b) - Decimal((delta**0.5)))) #aproximacao p*

    erro_absoluto = abs(x2 - float(real5))
    erro_relativo = erro_absoluto / abs(x2)

    return x1, x2, erro_relativo


def eq_2_grau(a, b, c): # para escolher a q tiver menos erro
    raiz, raizz, relativo1 = bhaskara(a, b, c)
    raiz1, raiz2, relativo = formula_alternativa(a, b, c)

    if relativo < relativo1:
        print("Para x1")
        chamada(raiz1)
        print("Para x2")
        chamada(raiz2)
    else:
        print("Para x1")
        chamada(raiz)
        print("Para x2")
        chamada(raizz)

'''if raizes is not None:
  print(f"Raízes: {raizes}")
else:
  print("Sem raízes reais")
'''


chamada(133 - 0.499) #a
eq_2_grau(1/3, 123/4, 1/6) #b
chamada(((13/14) - (6/7)) / ((2 * 2.718281828459045) - 5.4)) #c