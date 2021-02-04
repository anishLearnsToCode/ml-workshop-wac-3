"""
map(func, iterable_object)
"""

# numbers = [1, 2, 3, -10, 56]


def square(x: int) -> int:
    return x ** 2


# mapping = list(map(square, numbers))
# print(type(mapping))
# print(mapping)

numbers = list(map(int, input().split()))
print(numbers)


# for item in mapping:
#     print(item)
