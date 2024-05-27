#
def high_and_low(numbers):
    # ...
    numbers = sorted(int(x) for x in numbers.split())
    return f"{str(numbers[-1])} {str(numbers[0])}"


if __name__ == "__main__":
    """
    SCRIPT THAT RETURNS THE HIGHEST AND LOWEST NUMBER OF A ARRAY OF FOUR NUMBERS
    """
    resp = high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4")
    print(resp)
