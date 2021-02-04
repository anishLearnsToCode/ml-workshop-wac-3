def sum_squares(n: int) -> int:
    """:return 1^2 + 2^2 + ... + n^2"""
    sum = 0
    for i in range(1, n + 1):
        sum += i ** 2
    return sum


print(sum_squares(2))
