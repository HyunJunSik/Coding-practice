from collections import deque

a, k = map(int, input().split())
visited = [False] * (k+1)
result = [0] * (k+1)

q = deque([a])

while q:
    n = q.popleft()
    if n == k:
        print(result[k])
        break
    if not visited[n + 1]:
        visited[n + 1] = True
        q.append(n + 1)
        result[n + 1] = result[n] + 1
    if n * 2 < (k + 1):
        if not visited[n * 2]:
            visited[n * 2] = True
            q.append(n * 2)
            result[n * 2] = result[n] + 1