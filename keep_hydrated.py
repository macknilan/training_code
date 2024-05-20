#

def litres(time):
    """
    3 -> 1
    6.7 -> 3
    11.8 -> 5
    """
    return int(time) // 2


if __name__ == "__main__":
    """
    SCRIPT THAT CALCULATES HOW MANY LITRES OF WATER IN A GIVEN TIME 
    """
    resp = litres(2)
    print(resp)
