def not_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return True
    return False


num = int(input())

for i in range(1, num + 1):
    lower_bound, upper_bound = input().split()
    lower_bound = int(lower_bound)
    upper_bound = int(upper_bound)
    total = 0
    for k in range(lower_bound, upper_bound + 1):
        if k % 2 == 1 and not_prime(k):
            total = k + total
    print(total)
