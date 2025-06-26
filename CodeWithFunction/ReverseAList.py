def reverse_list(mylist):
    print("Before reversing:", mylist)
    rev = mylist[::-1]
    print("After reversing:", rev)
    return rev


def main():
    mylist = [10, 11, 12, 13, 14, 15]
    reverse_list(mylist)


main()
