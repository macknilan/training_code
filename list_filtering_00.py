# FUNCTION THAT RECEIVES A LIST OF INTEGERS
# NEGATIVE INTEGERS AND STRINGS AND RETURNS A LIST OF INTEGERS


def filter_list(l):
    """
    Function that takes a list of non-negative
    integers and strings and returns a new list
    with the strings filtered out.
    """
    # breakpoint()
    list_int = [x for x in l if type(x) is int]

    return list_int


if __name__ == "__main__":
    """
    FUNCTION THAT RECEIVES A LIST OF INTEGERS, NEGATIVE INTEGERS AND STRINGS
    AND RETURNS A LIST OF INTEGERS
    """
    list_int_str = input("Escribe una lista de números enteros y strings separados por coma -[1,2,'aasf','1','123',123]- : ")
    res = filter_list(eval(list_int_str))
    print(res)
