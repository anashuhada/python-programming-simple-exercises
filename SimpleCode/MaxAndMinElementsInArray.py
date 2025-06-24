# input: arr[] = {10, 20, 3}
# output: 20

arr = [11, 20, 30, 104, 95]

# finding max element
max = arr[0]  # assume first number is a max value
n = len(arr)

for i in range(1, n):
    if arr[i] > max:
        max = arr[i]

print("Maximum number is", max)

# finding min element
arr = [11, 20, 30, 104, 95]
min = arr[0]
n = len(arr)

for i in range(1, n):
    if arr[i] < min:
        min = arr[i]

print("Minimum number is", min)
