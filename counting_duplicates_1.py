#

def duplicate_count(text):
    return len([character for character in set(text.lower()) if text.lower().count(character) > 1])


if __name__ == "__main__":
    """
    SCRIPT TO COUNT DUPLICATES IN A STRING
    input: "Indivisibilities"
    output: 2
    """
    res = duplicate_count("Indivisibilities")
    print(res)









