from bisect import bisect_left, bisect_right
n = int(input())
arr = sorted(list(map(int, input().split())))
m = int(input())
arr2 = list(map(int, input().split()))
for i in range(m):
    start, end = 0, n - 1
    target = arr2[i]
    cnt = 0
    low = bisect_right(arr, target)
    high = bisect_left(arr, target)
    print(low - high,end=' ')