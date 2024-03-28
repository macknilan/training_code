# NUMERO CUADRADO PERFECTO
from math import sqrt


def is_square(n):
    if n < 0:
        return False
    elif n == 0:
        return True
    else:
        if (int(sqrt(n)) * int(sqrt(n)) == n) and (int(sqrt(n)) ** 2 == n):
            return True
        else:
            return False


if __name__ == "__main__":
    numero = int(input("Escribe un numero: "))
    res = is_square(numero)
    print(res)
