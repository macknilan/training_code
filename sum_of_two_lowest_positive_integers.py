#
def sum_two_smallest_numbers(numbers):
    """
    numbers: [19, 5, 42, 2, 77]
    return: 7
    """
    numbers = sorted(numbers)
    return numbers[0] + numbers[1]


if __name__ == "__main__":
    """
    SCRIPT THAT RETURNS THE LOWEST POSITIVE NUMBER OF A ARRAY OF FOUR NUMBERS
    """
    resp = sum_two_smallest_numbers([19, 5, 42, 2, 77])
    print(resp)

