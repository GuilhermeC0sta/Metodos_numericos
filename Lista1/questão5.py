def log2(x):
    if x <= 0:
        raise ValueError("O argumento de log2 deve ser maior que 0.")
    result = 0.0
    y = x
    if x < 1:
        while y < 1:
            result -= 1
            y *= 2
    elif x >= 2:
        while y >= 2:
            result += 1
            y /= 2
    z = (y - 1) / (y + 1)
    term = z
    n = 1
    while abs(term) > 1e-15:
        result += term
        n += 2
        term = (z ** n) / n
    return result

epsilon = 1.0
while 1.0 + epsilon != 1.0:
    epsilon /= 2.0
                                                  # esse dá 53
n = -log2(epsilon)
print(n)