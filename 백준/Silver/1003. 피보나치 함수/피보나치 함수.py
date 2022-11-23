def Ex1003():
    for i in range(int(input())):
        n = int(input())
        dp_0, dp_1 = [0] * (n + 2), [0] * (n + 2)
        dp_0[0],dp_1[0] = 1, 0
        dp_0[1],dp_1[1] = 0, 1
        if n < 2:
            print(dp_0[n], dp_1[n])
        else:
            for j in range(2, n + 1):
                dp_0[j] = dp_0[j - 1] + dp_0[j-2]
                dp_1[j] = dp_1[j - 1] + dp_1[j-2]
            print(dp_0[n], dp_1[n])

Ex1003()