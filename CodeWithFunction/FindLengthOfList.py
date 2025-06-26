def length_list(num):
    count = 0
    for i in num:
        count += 1
    print("Length of list:", count)
    return count


def main():
    num = [50, 6, 14, 32, 28, 71, 25, 99, 66]
    length_list(num)


main()
