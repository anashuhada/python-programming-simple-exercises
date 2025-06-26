def fibonacci_series(n1, n2):
    print(n1, n2)

    for i in range(2, 10):
        sum = n1 + n2
        print(sum, end=' ')
        n1 = n2
        n2 = sum
        

def main():
    fibonacci_series(0, 1)


main()
