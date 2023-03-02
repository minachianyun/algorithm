num = int(input())
for i in range(0, num):
    test = str(input())
    total = 1
    while total != "0" and int(test) >= 10:
        total = 0
        for k in test:
            total = int(k) ** 2 + total
        test = str(total)

    if test == "1":
        print("Happy")
    else:
        print("Not Happy")

