#

def to_jaden_case(string):

    # return = capitalized_words = [word.capitalize() for word in string.split()]
    return ' '.join([f"{word[0:1].upper()}{word[1:].lower()}" for word in string.split()])


if __name__ == "__main__":
    """
    SCRIPT THAT CAPITALIZE THE FIRST LETTER OF EACH WORD
    
    return: How Can Mirrors Be Real If Our Eyes Aren't Real
    """
    resp = to_jaden_case("How can mirrors be REAL if our EYES aren't real")
    print(resp)
