def run(string, sub_string):
    print(f"The values passed in the function are: {string} {sub_string}")

    if sub_string in string:
        print(f"The sub-string {sub_string} is in the string {string}")
        return True
    else:
        print(f"The sub-string {sub_string} is not in the string {string}")
        return False


if __name__ == "__main__":
    """
    THIS A MAIN FUNCTION
    THIS SCRIPT ONLY DO: CHECK IF A SUB-STRING ISA IN A STRING
    """

    input_str = input("Text input: ")
    input_sub_string = input("Sub-String text: ")
    print(f"Text -> {input_str}")
    print(f"Sub-string -> {input_sub_string}")

    run(input_str, input_sub_string)
