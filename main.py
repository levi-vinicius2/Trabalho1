def karatsuba(x, y):

    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    m = n // 2

    parte_alta1, parte_baixa1 = divmod(x, 10**m)
    parte_alta2, parte_baixa2 = divmod(y, 10**m)

    z0 = karatsuba(parte_baixa1, parte_baixa2)
    z1 = karatsuba((parte_baixa1 + parte_alta1), (parte_baixa2 + parte_alta2))
    z2 = karatsuba(parte_alta1, parte_alta2)

    return (z2 * 10**(2*m)) + ((z1 - z2 - z0) * 10**m) + z0


def main():
    num1 = 146123
    num2 = 352120
    resultado = karatsuba(num1, num2)
    print(f"O resultado de {num1} * {num2} é {resultado}")

if __name__ == "__main__":
    main()