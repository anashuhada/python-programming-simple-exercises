def sum_of_element(mylist):
    total = 0

    for i in range(0, len(mylist)):
        total += mylist[i]

    print("Sum:", total)

    print("Sum of all elements in given list:", sum(mylist))

    for x in mylist:
        total += x

    print("Sum:", total)

def main():
    mylist = [5, 10, 15, 50]
    sum_of_element(mylist)

main()