n = int(input())
dp = [0, 1]

for i in range(2, n + 1):
    minVal = 1e9
    for j in range(1, int(i**0.5) + 1):
        minVal = min(minVal, dp[i - j**2])
    dp.append(minVal + 1)
print(dp[n])