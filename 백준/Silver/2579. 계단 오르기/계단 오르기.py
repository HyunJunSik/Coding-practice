def Ex2579():
    # 계단오르기
    n = int(input())
    arr = [int(input()) for i in range(n)]
    dp = [0] * (n + 1)
    dp[1] = arr[0]
    if n > 1:
        dp[2] = arr[0] + arr[1]
    for i in range(3, n + 1):
        dp[i] = max(dp[i - 2] + arr[i - 1], dp[i - 3] + arr[i - 2] + arr[i - 1])
    print(dp[n])
Ex2579()