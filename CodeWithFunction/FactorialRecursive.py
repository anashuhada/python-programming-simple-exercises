def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


def main():
    num = 5
    print("Factorial of", num, "is", factorial_recursive(num))


main()
