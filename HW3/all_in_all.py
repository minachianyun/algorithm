test_case = int(input())

for i in range(0, test_case):
    first, second = input().split()
    lenf = len(first)
    lens = len(second)
    i = 0
    count = 0
    while i < lens and count < lenf:
        if second[i] == first[count]:
            count = count + 1
        i = i + 1
    if lenf == count:
        print("Yes")
    else:
        print("No")
