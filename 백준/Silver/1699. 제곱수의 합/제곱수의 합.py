def Ex1699():
    # 제곱수의 합
    n = int(input())
    dp = [i for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, i):
            if j * j > i:
                break
            dp[i] = min(dp[i], dp[i - j * j] + 1)
    print(dp[n])
Ex1699()