# SCRIPT REMOVE VOWELS IN A STRING

def disemvowel(string_):

    list_vowels = "aeiou"
    string_0 = "".join([char for char in string_ if char.lower() not in list_vowels])

    return string_0


if __name__ == "__main__":
    """
    SCRIPT REMOVE VOWELS IN A STRING
    """
    string = input("Escribe un string: ")
    res = disemvowel(string)
    print(res)

