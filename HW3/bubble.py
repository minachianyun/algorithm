from pip._vendor.distlib.compat import raw_input


def bubbleSort(test):
    length = len(test)
    swap = 0
    while length > 1:
        length = length - 1
        for i in range(0, length):
            if test[i] > test[i + 1]:
                t = test[i]
                test[i] = test[i + 1]
                test[i + 1] = t
                swap = swap + 1
    return swap


test_case = int(input())
for i in range(0, test_case):
    test_num = int(input())
    case = input().split()
    a = []
    for r in range(0, test_num):
        a.append(int(case[r]))
    print("Optimal swapping takes " + str(bubbleSort(a)) + " swaps.")
