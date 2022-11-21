n = int(input())
arr = sorted(list(map(int, input().split())))
cnt = 0
result = 0
for i in arr:
    result += (cnt + i)
    cnt += i
print(result)

