from collections import deque
arr = []
n = int(input())
for i in range(n):
    arr.append(list(input()))
visited = [[0] * n for i in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(c, row, col):
    global visited
    global arr
    q = deque([(row, col)])
    visited[row][col] = 1
    while q:
        (y, x) = q.popleft()
        for i in range(4):
            if y + dy[i] < n and y + dy[i] >= 0 and x + dx[i] < n and x + dx[i] >= 0:
                if visited[y + dy[i]][x + dx[i]] == 0 and arr[y + dy[i]][x + dx[i]] == c:
                    visited[y + dy[i]][x + dx[i]] = 1
                    q.append((y + dy[i], x + dx[i]))

color = ['R', 'G', 'B']
res = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(arr[i][j], i, j)
            res += 1
print(res, end=' ')
visited = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'
res = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(arr[i][j], i, j)
            res += 1
print(res)