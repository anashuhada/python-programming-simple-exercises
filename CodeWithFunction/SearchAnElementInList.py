def search_element(ele, mylist):
    flag = 0

    for i in mylist:
        if i == ele:
            print("Element found")
            flag = 1
            break
    if flag == 0:
        print("Element not found")

    # if ele in mylist:
    #     print("Element found")
    # else:
    #     print("Element not found")


def main():
    mylist = [1, 6, 3, 5, 3, 4]
    search_element(3, mylist)


main()
