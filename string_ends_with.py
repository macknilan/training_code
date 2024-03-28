#

def solution(str_1, str_2):
    if str_1.endswith(str_2):
        return True
    else:
        return False


if __name__ == "__main__":

    str_1 = input("Escribe un string: ")
    str_2 = input("String con las ultimas letras de primer string: ")
    res = solution(str_1, str_2)

