def factorial(n: int) -> int:
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def permutation(n: int, r: int) -> int:
    """:return nPr = n! / (n - r)!"""
    return factorial(n) // factorial(n - r)


def combination(n: int, r: int) -> int:
    """:return nCr = nPr / r!"""
    return permutation(n, r) // factorial(r)


# print(combination(5, 0))
# print(combination(5, 1))
# print(combination(5, 2))
# print(combination(5, 3))
# print(combination(5, 4))
# print(combination(5, 5))


for i in range(10):
    print(combination(9, i), end=' ')
