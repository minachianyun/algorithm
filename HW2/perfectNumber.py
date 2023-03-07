num = int(input())
test = input().split()
ans = []
for k in range(0, num):
    test_num = int(test[k])
    a = []
    for i in range(1, test_num):
        if (test_num % i) == 0:
            a.append(i)
    length = len(a)
    total = 0
    for r in range(0, length):
        total = total + a[r]
        if total == test_num:
            ans.append(test_num)

print(*ans)
