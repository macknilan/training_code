#


def calculate_years(principal, interest, tax, desired):
    """
    CALCULATE YEARS TO REACH DESIRED AMOUNT
    """
    if desired == principal:
        return 0

    years = 0
    print("DEBUGGER")
    while principal < desired:

        principal += (principal * interest) - (principal * interest * tax)
        years += 1
        print(f"P: {principal}")

    return years


if __name__ == "__main__":
    """
    SCRIPT THAT CALCULATES HOW MANY YEARS IT TAKES TO REACH A DESIRED AMOUNT
    P: PRINCIPAL MONEY TO INVEST
    Y: YEARS TO INVEST
    D: DESIRED AMOUNT IN THE FUTURE
    T: TAX RATE
    I: INTEREST RATE
    """
    resp = calculate_years(1000, 0.05, 0.18, 1100)
    print(resp)




