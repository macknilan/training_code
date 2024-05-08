#

def remove_smallest(numbers):
    if len(numbers) == 0:
        return []

    store_index = 0
    store_value = numbers[0]

    for i, v in enumerate(numbers):
        if v < store_value:
            store_value = v
            store_index = i
        print("DEBUGGER")
    new_numbers = numbers[:store_index] + numbers[store_index + 1:]

    return new_numbers


if __name__ == "__main__":
    """
    REMOVER EL MENOR ELEMENTO DE UNA LISTA, SIN MUTAR LA LISTA.
    SI HAY VARIOS ELEMENTOS IGUALES, REMOVER EL QUE TIENE MENOR INDICE(PRIMERO)
    """
    resp = remove_smallest([1, 2, 3, 4, 5])
    print(resp)




