#
def round_to_next5(n):
    """
    input:    output:
    0    ->   0
    2    ->   5
    3    ->   5
    12   ->   15
    21   ->   25
    30   ->   30
    -2   ->   0
    -5   ->   -5
    """

    if n == 0:
        return 0
    if n % 5 == 0:
        return n * 1
    else:
        return (n // 5 + 1) * 5


if __name__ == "__main__":
    """
    SCRIPT THAT ROUNDS A NUMBER TO THE NEXT MULTIPLE OF 5
    """
    resp = round_to_next5(5)
    print(resp)





