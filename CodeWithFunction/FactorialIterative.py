def factorial_iterative(fac, num):
    if num < 0:
        print("Factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1, num + 1):
            fac *= i
        print("The factorial of", num, "is", fac)


def main():
    factorial_iterative(1, 5)


main()
