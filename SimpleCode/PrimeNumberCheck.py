# Natural Number: 1
# Which has only 2 factors 1 and itself
# Should be divided by 1 and it's number
# 19 => 1 and 19

num = 21
count = 0

if num > 1:
    for i in range(1, num + 1):
        if num % i == 0:
            count = count + 1
    if count == 2:
        print("Number is prime")
    else:  # more than 2 factors
        print("Number is not prime")

arr_num = [1, 3, 15, 9, 21, 5]

for i in range(0, len(arr_num)):
    count = 0
    for num in range(1, arr_num[i] + 1):
        if arr_num[i] % num == 0:
            count += 1
    if count == 2:
        print(arr_num[i], "is prime number")
    else:  # more than 2 factors
        print(arr_num[i], "is not prime number")
