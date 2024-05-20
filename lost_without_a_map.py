#

def maps(a):
    """
    [1, 2, 3] --> [2, 4, 6]
    """
    return list(map(lambda x: x * 2, a))


if __name__ == "__main__":
    """
    DE UN ARRAY DE NÚMEROS ENTEROS DEVOLVER UN ARRAY CON CADA NUMERO MULTIPLICADO POR 2
    """

    resp = maps([1, 2, 3])
    print(resp)
