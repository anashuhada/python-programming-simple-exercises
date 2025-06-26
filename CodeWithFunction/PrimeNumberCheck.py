def single_num(num):
    count = 0

    if num > 1:
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
        if count == 2:
            print("Number is prime")
        else:
            print("Number is not prime")


def multiple_num(arr_num):
    for i in range(1, len(arr_num)):
        count = 0
        for num in range(1, arr_num[i] + 1):
            if arr_num[i] & num == 0:
                count += 1
        if count == 2:
            print(arr_num[i], "is prime number")
        else:
            print(arr_num[i], "is not prime number")


def main():
    single_num(3)
    arr_num = [1, 3, 15, 9, 21, 5]
    multiple_num(arr_num)


main()
