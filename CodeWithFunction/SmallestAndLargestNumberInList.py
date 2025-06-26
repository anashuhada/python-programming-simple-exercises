def smallest_and_largest(mylist):
    mylist.sort()
    print(mylist)
    print("Smallest element is:", mylist[0])
    print("Largest element is:", mylist[-1])

    first, last = 0, -1
    print("Smallest element is:", mylist[first])
    print("Largest element is:", mylist[last])

    print("Smallest element is:", min(mylist))
    print("Largest element is:", max(mylist))


def main():
    mylist = [20, 100, 20, 1, 10]
    smallest_and_largest(mylist)


main()
