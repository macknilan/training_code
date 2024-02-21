#


def vowel_indices(word):
    """
    FUNCTION TO FIND DE INDEX OF VOWELS IN A WORD
    """
    list_vowels = "aeiou"

    resp_list = [
        idnex for idnex, char in enumerate(word.lower(), 1) if char in list_vowels
    ]

    return resp_list


if __name__ == "__main__":
    input_str = input("Text input: ")
    resp = vowel_indices(input_str)
    print(f"resp -> {resp}")
