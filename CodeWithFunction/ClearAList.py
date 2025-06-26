def clear_a_list(mylist):
    print("Before clearing mylist:", mylist)
    # mylist.clear()
    # mylist = []
    mylist *= 0
    print("After clearing mylist:", mylist)


def main():
    mylist = [6, 0, 4, 1]
    clear_a_list(mylist)


main()
