import math

num = int(input())

for i in range(1, num+1):
    first, second = input().split()
    first = int(first)
    second = int(second)
    print(math.gcd(first, second))

