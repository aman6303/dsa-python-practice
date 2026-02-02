def calculate_power(n, k):

    if k == 1:
        return n

    return n * calculate_power(n, k - 1)


print(calculate_power(8, 2))
