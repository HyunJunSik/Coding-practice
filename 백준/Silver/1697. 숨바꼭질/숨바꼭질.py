N, K = map(int, input().split())
dp = [0] * 100001
for i in range(N - 1, -1, -1):
    dp[i] = dp[i + 1] + 1
for i in range(N + 1, 100001):
    dp[i] = dp[i - 1] + 1
for _ in range(3):
    for i in range(N, 100000):
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i - 1] + 1, dp[i // 2] + 1, dp[i + 1] + 1)
        else:
            dp[i] = min(dp[i], dp[i - 1] + 1, dp[i + 1] + 1)
    dp[100000] = min(dp[100000], dp[99999] + 1, dp[50000] + 1) 
print(dp[K])