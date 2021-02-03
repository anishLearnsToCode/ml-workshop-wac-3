"""
N
1 + 2 + 3 + ... + N
N = 0 --> 0
N = 1 --> 1
N = 3 --> 1 + 2 + 3 = 6
"""

N = int(input())

i = 1
result = 0

while i <= N:
    result += i
    i += 1

print(result)


"""
N = 0
i = 1
result = 0
0
"""
