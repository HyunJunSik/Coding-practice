from collections import deque

def bfs(graph, v, visited):
    global result
    q = deque([v])
    visited[v] = True
    while q:
        v = q.popleft()
        result.append(v)
        for i in range(len(graph)):
            if graph[v][i] and (not visited[i]):
                q.append(i)
                visited[i] = True

def dfs(graph, v, visited):
    global result
    visited[v] = True
    result.append(v)
    for i in range(len(graph)):
        if graph[v][i] and (not visited[i]):
            dfs(graph, i, visited)

n, m, v = map(int, input().split())
G = [[0] * (n + 1) for i in range(n + 1)]
for i in range(m):
    s, e = map(int, input().split())
    G[s][e] = 1 ; G[e][s] = 1
for j in range(2):
    visited = [False] * (n + 1)
    result = []
    if j == 0:
        dfs(G, v, visited)
        print(*result)
    else:
        bfs(G, v, visited)
        print(*result)
