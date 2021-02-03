"""
N! = 1 * 2 * 3 * ... * N
0! = 1! = 1
"""

N = int(input())

i = 1
result = 1

while i <= N:
    result *= i
    i += 1

print(result)


"""
N = 0
i = 1
result = 1
1
"""
