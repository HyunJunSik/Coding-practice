dp = []
for i in range(int(input())):
    dp.append(list(map(int, input().split())))
for i in range(1, len(dp)):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + dp[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + dp[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + dp[i][2]
print(min(dp[len(dp)-1]))