case = int(input())
while case != 0:
    try:
        n = int(input())
    except EOFError:
        break

    row = (n-1)/2 + 1  # 第幾列
    row_num = 1 + (row-1) * 2 # 所求該列有幾個數值
    total_num = ((1 + row_num)*row) / 2
    total_num = int(total_num)
    last = 1 + (total_num - 1) * 2 # 最後一個數值
    ans = last * (last-2) * (last-4)
    print(ans)
    case = case - 1
