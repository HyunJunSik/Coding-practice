dp = [1, 1, 1]
for i in range(3, 101):
    dp.append(dp[i - 2] + dp[i - 3])
for i in range(int(input())):
    print(dp[int(input()) - 1])
