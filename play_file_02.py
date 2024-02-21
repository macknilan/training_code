from collections import Counter


def main(input_str):
    resp_list = []
    most_common_text = Counter(input_str).most_common()

    # print(f"most_common_text -> {most_common_text}")

    list_vowels = ["a", "e", "i", "o", "u"]
    for vowel in list_vowels:
        # print(f"vowel -> {vowel}")
        for i, v in enumerate(most_common_text):
            if vowel == v[0] or vowel.upper() == v[0]:
                resp_list.append(v)

    # ORDER THE LIST OF TUPLE WITH A LAMBDA FUNCTION
    resp_list = sorted(resp_list, key=lambda x: x[1], reverse=True)[0]

    return resp_list


if __name__ == "__main__":
    """
    SCRIPT FOR COUNTING HOW MANY TIMES A VOWELS APPEARS IN A TEXT
    """
    input_str = input("Text input: ")
    resp = main(input_str)
    print(f"resp -> {resp}")
