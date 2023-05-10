import sys
arr = []
ans = []

def check_can(arr, target):
    t = 0
    want = 0
    for i in arr:
        if target > i:
            t += (target - i)
            want -= (target - i)
        elif target < i:
            t += 2 * (i - target)
            want += (i - target)
    return t, want

n, m, b = map(int, sys.stdin.readline().split())

for i in range(n):
    arr2 = list(map(int, sys.stdin.readline().split()))
    for j in arr2:
        arr.append(j)
        
min_num, max_num = min(arr), max(arr)

for i in range(min_num, max_num + 1):
    t, want = check_can(arr, i)
    if want + b >= 0:
        ans.append((t, i))
ans = sorted(ans, key=lambda ans : ans[0])
arr = []
for i in ans:
    arr.append(i[0])
num = min(arr)
arr = []
for i in ans:
    if i[0] == num:
        arr.append(i[1])
num2 = max(arr)
print(num, num2)