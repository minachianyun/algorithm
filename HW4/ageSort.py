num = 1
while num != 0:
    num = int(input())
    if num == 0:
        break
    test = input().split()
    a = []
    for i in range(0, num):
        a.append(int(test[i]))
    a.sort()
    print(*a)