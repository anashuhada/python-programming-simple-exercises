def swap_two_elements(mylist):
    print(mylist)
    element1, element2 = 1, 3
    mylist[element1], mylist[element2] = mylist[element2], mylist[element1]
    print(mylist)


def main():
    mylist = [23, 65, 19, 90]
    swap_two_elements(mylist)


main()
