for i in range(int(input())):
    n = int(input())
    dp = [0] * (n + 3)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for j in range(4, n + 1):
        dp[j] = dp[j-1]+dp[j-2]+dp[j-3]
    print(dp[n])