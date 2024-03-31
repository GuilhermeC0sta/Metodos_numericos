def erros(p, pl):
    erro_absoluto = abs(p - pl)
    erro_relativo = erro_absoluto / abs(p)

    print(f'p = {p} e pl = {pl}')
    print("Erro Absoluto: ", erro_absoluto)
    print(f'Erro Relativo: {erro_relativo}\n')

erros(1, 0.9994) #a
erros(124, 7) #b
erros(2.718281828459045235360287**10, 22000) #c
resultado=1
count=1

while count <= 8:
    resultado = resultado * count
    count += 1
erros(resultado, 39900) #d
