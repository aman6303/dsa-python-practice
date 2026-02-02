def numbers(n):
    if n == 1:
        print(1)
        return

    print(n, end=" ")
    numbers(n - 1)


numbers(10)
