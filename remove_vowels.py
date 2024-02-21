def shortcut(s):
    list_vowels = "aeiou"

    list_characters = [
        char for index, char in list(enumerate(cadena)) if char in list_vowels
    ]

    for x in list_characters:
        s = s.replace(x, "")

    return s


if __name__ == "__main__":
    """
    SCRIPT FOR REMOVING VOWELS FROM A TEXT
    """
    cadena = input("Text input: ")
    resp = shortcut(cadena)
    print(f"resp -> {resp}")
