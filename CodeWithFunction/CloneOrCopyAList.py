def clone_or_copy_list(mylist):
    print(mylist)
    # new_list = mylist.copy()
    new_list = mylist[:]
    print("mylist is copied:", new_list)


def main():
    mylist = [4, 8, 2, 10, 15, 18]
    clone_or_copy_list(mylist)


main()
