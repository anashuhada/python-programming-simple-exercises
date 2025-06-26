def max_element(arr):
    print(arr)
    print(len(arr))
    max = arr[0]

    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]

    print("Maximum number is", max)


def min_element(arr):
    min = arr[0]

    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]

    print("Minimum number is", min)


def main():
    arr = [11, 20, 30, 104, 95, 5]
    max_element(arr)
    min_element(arr)


main()
