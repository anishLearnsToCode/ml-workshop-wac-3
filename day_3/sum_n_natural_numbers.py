def sum_n_natural_numbers(n: int) -> int:
    """:return 1 + 2 + 3 + .. + n"""
    # result = 0
    # for i in range(1, n + 1):
    #     result += i
    # return result
    return n * (n + 1) // 2


def subtraction(a: int, b: int) -> int:
    return a - b


# a = 10, b = 5
def addition(a: int, b: int) -> int:
    return a + b


print(addition(10, 5))
# print(15)
