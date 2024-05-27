#
def make_negative(number):
    """
    1 -> -1
    -5 -> -5
    0 -> 0
    """
    return number * -1 if number > 0 else number


if __name__ == "__main__":
    """
    SCRIPT THAT RETURNS ANY NUMBER AND MAKE IT NEGATIVE
    """
    resp = make_negative(-9)
    print(resp)
