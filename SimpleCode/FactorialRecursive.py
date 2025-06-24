# 5 * (5-1) * (4-1) * (3-1) * (2-1) = 120

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

    # ternary operator
    # return 1 if n == 0 or n == 1 else n * factorial(n - 1)


num = 5
print("Factorial of", num, "is", factorial(num))
