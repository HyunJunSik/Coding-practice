w,l,d = map(float, input().split())
dp = [[0] * 21 for i in range(41)]
dp[20][0] = 1

for i in range(1, 21):
    for j in range(1, 40):
        dp[j][i] = dp[j - 1][i - 1] * w + dp[j][i - 1] * d + dp[j + 1][i - 1] * l
    dp[0][i] = dp[0][i - 1] * d + dp[1][i - 1] * l
    dp[40][i] = dp[39][i - 1] * w + dp[40][i - 1] * d

for i in range(0, 40, 10):
    result = 0
    for j in range(i, i + 10):
        result += dp[j][20]
    print(format(result, '.8f'))
print(format(dp[40][20], '.8f'))