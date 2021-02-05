import random

a, b = -100, 100
# r = int((b - a) * random.random() + a)
# print(r)

print(random.randint(a, b))


"""
(0, 1) * 10
(0, 10)

(0, 1) * 2
(0, 2) + 8
(8, 10)

(0, 1) * (b - a)
(0, b - a) + a
(a, b)
"""
