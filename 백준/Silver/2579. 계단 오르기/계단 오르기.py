def Ex2579():
    n = int(input())
    arr = []
    dp = [0] * (n + 1)
    for i in range(n):
        arr.append(int(input()))
    dp[1] = arr[0]
    if n > 1:
        dp[2] = arr[1] + arr[0]
    for i in range(3, n + 1):
        dp[i] = max(dp[i - 2], arr[i - 2] + dp[i - 3]) + arr[i - 1]
    print(dp[-1])
Ex2579()