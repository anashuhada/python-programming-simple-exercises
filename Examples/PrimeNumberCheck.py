# Natural Number: 1
# Which has only 2 factors 1 and itself
# Should be divided by 1 and it's number
# 19 => 1 and 19

num = 21
count = 0

if num > 1:
    for i in range(1, num + 1):
        if (num % i) == 0:
            count = count + 1
    if count == 2:
        print("Number is prime")
    else: # more than 2 factors
        print("Number is not prime")
