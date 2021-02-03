"""
N
1^2 + 2^2 + 3^2 + ... + N^2
"""

N = int(input())
sum = 0

for i in range(1, N + 1):
    sum += i ** 2

print(sum)
