#
def replace_exclamation(s):
    list_vowels = "aeiou"
    list_chars = [
        cadena[index] for index, val in enumerate(cadena.lower()) if val in list_vowels
    ]

    for c in list_chars:
        s = s.replace(c, "!")

    return s


if __name__ == "__main__":
    """
    SCRIPT FOR REPLACING VOWELS WITH EXCLAMATIONS
    """
    input_str = input("Text input: ")
    resp = replace_exclamation(input_str)
    print(f"resp -> {resp}")
