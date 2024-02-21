#


def even_or_odd(number):
    resp = "Even" if number % 2 == 0 else "Odd"

    return resp


if __name__ == "__main__":
    """
    SCRIPT TO DETERMINE IF A NUMBER IS EVEN OR ODD
    """
    input_str = input("Number input:")
    resp = even_or_odd(int(input_str))
    print(f"resp -> {resp}")
