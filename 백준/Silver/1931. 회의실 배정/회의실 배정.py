n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
arr = sorted(arr, key = lambda x : x[0])
arr = sorted(arr, key = lambda x : x[1])
e, cnt = 0, 0
for i in arr:
    if e <= i[0]:
        cnt += 1
        e = i[1]
print(cnt)