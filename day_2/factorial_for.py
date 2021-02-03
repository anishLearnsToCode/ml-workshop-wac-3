"""
N!= 1 * 2 * 3 * ... * N
0! = 1! = 1
"""

N = int(input())
result = 1

for i in range(2, N + 1):
    result = result * i

print(result)
