#
def check_vowel(strng, position):
    list_vowels = "aeiou"
    index_vowels = [
        index for index, char in list(enumerate(strng)) if char.lower() in list_vowels
    ]

    if position < 0:
        return False
    elif position in index_vowels:
        return True
    else:
        return False


if __name__ == "__main__":
    """
    SCRIPT FOR CHECKING IF A VOWEL IS IN A POSITION
    """
    input_str = input("Text input: ")
    position = int(input("Position: "))
    resp = check_vowel(input_str, position)
    print(f"resp -> {resp}")
