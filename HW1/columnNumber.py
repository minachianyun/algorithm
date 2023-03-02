num = int(input())

for i in range(0, num):
    test = str(input())
    l = len(test)
    total = 0
    for k in test:
        if (k == "A"):
            r = 1
        elif (k == "B"):
            r = 2
        elif (k == "C"):
            r = 3
        elif (k == "D"):
            r = 4
        elif (k == "E"):
            r = 5
        elif (k == "F"):
            r = 6
        elif (k == "G"):
            r = 7
        elif (k == "H"):
            r = 8
        elif (k == "I"):
            r = 9
        elif (k == "J"):
            r = 10
        elif (k == "K"):
            r = 11
        elif (k == "L"):
            r = 12
        elif (k == "M"):
            r = 13
        elif (k == "N"):
            r = 14
        elif (k == "O"):
            r = 15
        elif (k == "P"):
            r = 16
        elif (k == "Q"):
            r = 17
        elif (k == "R"):
            r = 18
        elif (k == "S"):
            r = 19
        elif (k == "T"):
            r = 20
        elif (k == "U"):
            r = 21
        elif (k == "V"):
            r = 22
        elif (k == "W"):
            r = 23
        elif (k == "X"):
            r = 24
        elif (k == "Y"):
            r = 25
        elif (k == "Z"):
            r = 26
        total = r*(26**(l-1)) + total
        l = l - 1
    print(total)
