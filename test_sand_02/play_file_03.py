from collections import Counter


def main(input_str):
    list_vowels = "aeiou"

    resp_vowels = len([char for char in input_str if char in list_vowels])

    return resp_vowels


if __name__ == "__main__":
    """
    SCRIPT FOR COUNTING HOW MANY TIMES THE VOWELS APPEARS IN A TEXT
    """
    input_str = input("Text input: ")
    resp = main(input_str)
    print(f"resp -> {resp}")
