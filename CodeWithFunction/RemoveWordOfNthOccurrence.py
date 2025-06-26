def remove_occurrence(which_element, num, mylist):
    count = 0

    for i in range(0, len(mylist)):
        if mylist[i] == which_element:
            count += 1
            if count == num:
                del mylist[i]
                break

    print(mylist)


def main():
    mylist = ["geeks", "for", "geeks", "geeks"]
    remove_occurrence("geeks", 1, mylist)


main()
