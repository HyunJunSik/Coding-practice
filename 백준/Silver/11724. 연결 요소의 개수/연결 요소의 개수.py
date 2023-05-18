from collections import deque

def bfs(graph, v):
    global visited
    q = deque([v])
    visited[v] = True
    
    while q:
        v = q.popleft()
        for i in range(1, len(graph)):
            if graph[v][i] and (not visited[i]):
                q.append(i)
                visited[i] = True

n, m = map(int, input().split())
visited = [False] * (n + 1)
visited[0] = True
arr = [[0] * (n + 1) for i in range(n + 1)]

for i in range(m):
    v, w = map(int, input().split())
    arr[v][w] = 1
    arr[w][v] = 1

cnt = 0
for i in range(1, n + 1):
    if visited[:] == True:
        break
    if visited[i] == False:
        cnt += 1
        bfs(arr, i)
print(cnt)

