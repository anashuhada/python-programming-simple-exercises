def multiple_numbers(mylist):
    count = 1

    for i in mylist:
        count *= i

    print("Multiply result:", count)


def main():
    mylist = [3, 2, 4]
    multiple_numbers(mylist)


main()
