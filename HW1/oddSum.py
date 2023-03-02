num = int(input())

for i in range(1,num+1):
    lower_bound = int(input())
    upper_bound = int(input())
    total = 0
    for k in range(lower_bound, upper_bound+1):
        if k%2 == 1:
            total = k + total
    print("Case " + str(i) + ": " + str(total))



