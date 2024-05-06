#
def reverse_list(l):
    l = l[::-1]

    return l


if __name__ == "__main__":
    """
    SCRIPT THAT RECEIVES A LIST AND RETURN A LIST WITH THE REVERSE ORDER OF L
    """
    res = reverse_list([1, 2, 3, 4, 5])
    print(res)

