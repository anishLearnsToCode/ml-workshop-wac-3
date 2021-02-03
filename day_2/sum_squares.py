"""
N
1^2 + 2^2 + 3^2 + ... + N^2
1^3 + 2^3 + ... + N^3
"""

N = int(input())

i = 1
result = 0

while i <= N:
    result += i ** 2
    i += 1

print(result)


"""
N = 2

"""
