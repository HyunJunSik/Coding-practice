from collections import deque

n, m = map(int, input().split())
arr = [0] * 101
visited = [False] * 101
r = dict()
s = dict()

for i in range(n):
    a, b = map(int, input().split())
    r[a] = b
for i in range(m):
    a, b = map(int, input().split())
    s[a] = b

q = deque([1])

while q:
    loc = q.popleft()
    if loc == 100:
        break
    for i in range(1, 7):
        next_loc = loc + i
        if next_loc <= 100 and not visited[next_loc]:
            if next_loc in r.keys():
                next_loc = r[next_loc]
            if next_loc in s.keys():
                next_loc = s[next_loc]
            if not visited[next_loc]:
                visited[next_loc] = True
                arr[next_loc] = arr[loc] + 1
                q.append(next_loc)
print(arr[100])
            