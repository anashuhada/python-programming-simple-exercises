def search_second_largest_number(mylist):
    print(mylist)
    mylist.sort()
    print(mylist)
    print(mylist[-1])
    print(mylist[-2])  # 45


def main():
    mylist = [10, 20, 4, 45, 99]
    search_second_largest_number(mylist)


main()
