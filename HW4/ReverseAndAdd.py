# 檢查是否迴文
def palindrome(test_case):
    if str(test_case) == str(test_case)[::-1]:
        return True
    else:
        return False

case = int(input())
for i in range(0, case):
    test = input()
    a = int(test)
    b = int(test[::-1])
    sum = a + b
    count = 1
    while palindrome(sum)==False:
        count = count + 1
        test = str(sum)
        a = sum
        b = int(test[::-1])
        sum = a + b

    # palindrome == True 迴文
    print(str(count) + " " + str(sum))
