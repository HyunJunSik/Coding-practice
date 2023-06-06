n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n):
            if (arr[i][k] + arr[k][j]) > 1:
                arr[i][j] = 1
for i in range(n):
    print(*arr[i])