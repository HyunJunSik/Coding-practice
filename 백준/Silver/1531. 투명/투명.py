arr = [[0] * 101 for i in range(101)]
n, m = map(int, input().split())
for _ in range(n):
    x_d, y_d, x_u, y_u = map(int, input().split())
    for x in range(x_d, x_u + 1):
        for y in range(y_d, y_u + 1):
            arr[y][x] += 1
result = 0
for i in range(1, 101):
    for j in range(1, 101):
        if arr[j][i] > m:
            result += 1
print(result)
