for i in range(int(input())):
    m, n, x, y = map(int, input().split())
    k = x
    flag = False
    while k <= m * n:
        if (k - x) % m == 0 and (k - y) % n == 0:
            flag = True
            break
        k += m
    print(k if flag else -1)