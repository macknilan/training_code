#

def duplicate_count(text):
    if len(text) == 0:
        return 0
    text = text.lower()
    text_repeticions = []
    for i, v in enumerate(text):
        for x in text[i+1:]:
            if v == x and x not in text_repeticions:
                text_repeticions.append(x)

    return len(text_repeticions)


if __name__ == "__main__":
    """
    SCRIPT TO COUNT DUPLICATES IN A STRING
    input: "Indivisibilities"
    output: 2
    """
    res = duplicate_count("Indivisibilities")
    print(res)









