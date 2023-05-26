from itertools import combinations
S = int(input())
S_in = list(map(int, input().split()))
arr = [0] * (max(S_in) + 1)
for i in S_in:
    arr[i] = 1
n = int(input())

if n in S_in:
    print(0)
else:
    result = 0
    min_num = 1
    for i in range(n - 1, 0, -1):
        if arr[i] == 1:
            min_num = i + 1
            break
    for i in range(n + 1, max(S_in) + 1):
        if arr[i] == 1:
            break
    max_num = i - 1
    possible = list(combinations(range(min_num, max_num + 1), 2))
    for pos in possible:
        min_pos = pos[0]; max_pos = pos[1]
        if min_pos <= n and max_pos >= n:
            result += 1
    print(result)

