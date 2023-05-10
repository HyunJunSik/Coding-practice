arr = []
for i in range(int(input())):
    x, y = map(int, input().split())
    arr.append((x, y))
for i in range(len(arr)):
    (x_1, y_1) = arr[i]
    cnt = 0
    for j in range(len(arr)):
        if i == j:
            continue
        (x_2, y_2) = arr[j]
        if x_2 > x_1 and y_2 > y_1:
            cnt += 1
    print(cnt + 1, end=' ')