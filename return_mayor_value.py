# SCRIPT FOR GET THE MAYOR VALUE OF THREE NUMBERS


def get_grade(s1, s2, s3):

    average = (s1 + s2 + s3) / 3

    if 90 <= average <= 100:
        return "A"
    if 80 <= average <= 90:
        return "B"
    if 70 <= average <= 80:
        return "C"
    if 60 <= average <= 70:
        return "D"
    if 0 <= average <= 60:
        return "F"


if __name__ == "__main__":
    """
    SCRIPT FOR GET THE MAYOR VALUE OF THREE NUMBERS
    """
    s1 = int(input("Escribe un numero: "))
    s2 = int(input("Escribe un numero: "))
    s3 = int(input("Escribe un numero: "))
    res = get_grade(s1, s2, s3)
    print(res)

