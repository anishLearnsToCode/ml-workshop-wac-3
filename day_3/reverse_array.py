_ = input()
numbers = list(map(int, input().split()))
numbers = numbers[::-1]

for element in numbers:
    print(element, end=' ')
