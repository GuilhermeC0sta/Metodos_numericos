from decimal import Decimal

#n = (121 - 119) - 0.327 #d
n = (2/9) * (9/7) #g
#n = 133 + 0.921 #a
#n = 133 - 0.499 #b

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
        print(int(num))
    else:
        print(num)

def truncamento_3_digitos(n):
    num_int = contar_algarismos_inteiros(n) #10³, somente o expoente, sem o 10
    print(num_int)
    n_string = str(n / 10**num_int) # 0.133921

    n_string = n_string[0] + n_string[1] + n_string[2] + n_string[3] + n_string[4] # pega os 3 digitos
    print(n_string)

    trunc3 = Decimal(float(n_string) * 10**num_int) #Decimal deixa o numero com varios digitos, e nao somente 3
    print(trunc3)

    n_string = str(trunc3)
    if len(n_string) > 4:
        n_string = n_string[0] + n_string[1] + n_string[2] + n_string[3] + n_string[4] # pega os 3 digitos dnv

    trunc3digit = float(n_string)

    imprimir_numero(trunc3digit)

truncamento_3_digitos(n)
