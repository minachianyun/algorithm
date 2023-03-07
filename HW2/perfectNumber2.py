def perfect_number(n):
    total = 0
    for x in range(1, n):
        if n % x == 0:
            total = total + x
    return total == n


num = int(input())
test = input().split()
ans = []
for k in range(0, num):
    test_num = int(test[k])
    if perfect_number(test_num):
        ans.append(test_num)

print(*ans)
