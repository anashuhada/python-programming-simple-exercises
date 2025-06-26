def swap_first_and_last_element(mylist):
    print(mylist)
    # mylist[0], mylist[-1] = mylist[-1], mylist[0]
    # print(mylist)

    start, *middle, end = mylist
    mylist = [end, *middle, start]
    print(mylist)


def main():
    mylist = [93, 79, 15, 23, 30]
    swap_first_and_last_element(mylist)


main()
