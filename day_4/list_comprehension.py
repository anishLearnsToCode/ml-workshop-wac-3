"""
{x | x in (-10, 10)}
{x^2 | x in (0, 5)}

(f(var) for variable in iterable)
"""

# g = [i ** 2 for i in range(1, 11)]
# print(type(g))
# print(g)

# print([character for character in input()])

# print(max([1, 2, 3, 4, 5]))
# print(min([1, 2, 3, 4, 5]))
# print(sum([i for i in range(1, 11)]))

n = int(input())
print(sum(i for i in range(1, n + 1)))
