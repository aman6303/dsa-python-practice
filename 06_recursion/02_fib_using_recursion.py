# 1 1 2 3 5 8 13.....


def calculate_fib(n):

    if n == 1 or n == 2:
        return 1

    return calculate_fib(n - 1) + calculate_fib(n - 2)


print(calculate_fib(7))
