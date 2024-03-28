#

def square_sum(numbers):
    list_str_num = [x*-1 if x < 0 else x for x in numbers]
    # list_str_num = [x * x for x in numbers]

    list_num = sum([num*num for num in list_str_num])

    return list_num


if __name__ == "__main__":
    """
    SCRIPT THAT RECEIVES A LIST OF INTEGER NUMBER AND SUM THE SQUARE OF EACH NUMBER
    """
    list_numbers = input("Escribe una lista de números separados por coma: ")
    res = square_sum(list_numbers)
    print(res)




