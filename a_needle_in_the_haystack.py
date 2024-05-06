# SCRIPT PARA ENCONTRAR EL INDICE DE UNA LISTA DE STRINGS LA PALABRA "NEEDLE"

def find_needle(haystack):
    for x in haystack:
        if x == "needle":
            return f"found the needle at position {haystack.index(x)}"
    return "No needle found"


if __name__ == "__main__":
    """
    SCRIPT THAT RECEIVES A LIST OF STRINGS AND SEARCHES FOR THE WORD "NEEDLE"
    """
    list_str = input("Escribe una lista de strings separados por coma ejem -['moreJunk', 'needle', 'randomJunk']- : ")
    res = find_needle(eval(list_str))
    print(res)














