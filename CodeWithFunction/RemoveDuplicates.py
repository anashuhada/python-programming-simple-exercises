def find_duplicate_numbers(mynumber):
    print(mynumber)
    is_duplicate = []
    count = 0

    for i in mynumber:
        if mynumber.count(i) > 1 and i not in is_duplicate:
            is_duplicate.append(i)
            count += 1

    print("Total count of duplicates:", count, ", string duplicated:", is_duplicate)


def find_duplicate_words(mylist):
    print(mylist)
    is_duplicate = []
    count = 0

    for i in mylist:
        if mylist.count(i) > 1 and i not in is_duplicate:
            is_duplicate.append(i)
            count += 1

    print("Total count of duplicates:", count, ", number duplicated:", is_duplicate)


def main():
    mynumber = [20, 55, 96, 61, 33, 52, 55, 20]
    find_duplicate_numbers(mynumber)
    mylist = ["geeks", "for", "geeks", "geeks"]
    find_duplicate_words(mylist)


main()
