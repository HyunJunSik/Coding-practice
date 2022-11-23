def Ex2():
    arr = [list(map(int, input().split())) for i in range(int(input()))]
    dp = [[0] * len(arr) for i in range(len(arr))]
    dp[0][0] = arr[0][0]

    for i in range(1, len(arr)):
        for j in range(i + 1):
            if j == 0:
                dp[i][j] = arr[i][j] + dp[i-1][j]
            elif j == i:
                dp[i][j] = arr[i][j] + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i][j], arr[i][j] + dp[i-1][j-1], arr[i][j] + dp[i-1][j])
    print(max(dp[-1]))

Ex2()