def count_occurrences(mylist):
    which_element = 10
    count = 0

    for i in mylist:
        if i == which_element:
            count += 1
    print(which_element, "has", count, "times in mylist")

    print(which_element, "has", mylist.count(which_element), "times in mylist")


def main():
    mylist = [15, 6, 7, 10, 12, 20, 10, 28, 10, 20]
    count_occurrences(mylist)


main()
