# 5! = 1 * 2 * 3 * 4 * 5 = 120

fac = 1
num = 5

if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        fac = fac * i  # i = 1, 2, 3
    print("The factorial of", num, "is", fac)
