def swap_two_numbers(a, b):
    print("Before swapping", a, b)

    # temp = a
    # a = b
    # b = temp

    a, b = b, a

    print("After swapping", a, b)


def main():
    swap_two_numbers(50, 100)


main()
