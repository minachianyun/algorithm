case = int(input())
for i in range(0, case):
    # 字串的長度: length
    # 字串的數目: num
    length, num = input().split()
    length = int(length)
    num = int(num)
    A = 1
    C = 2
    G = 3
    T = 4
    dic = {}
    for k in range(0, num):
        test = input()
        count = 0
        for r in range(0, length):
            for l in range(r + 1, length):
                if test[r] > test[l]:
                    count = count + 1
        dic[test] = count
    sorted_dic = {}
    sorted_keys = sorted(dic, key=dic.get)
    for element in sorted_keys:
        print(element)

    if i == (case - 1):
        break
    else:
        print()
        input()
