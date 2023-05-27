from collections import deque
arr = []
n = int(input())
for i in range(n):
    arr.append(input())
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
        for dir in range(4):
            if y + dy[dir] < n and y + dy[dir] >= 0 and x + dx[dir] < n and x + dx[dir] >= 0:
                if visited[y + dy[dir]][x + dx[dir]] == 0 and arr[y + dy[dir]][x + dx[dir]] == c:
                    visited[y + dy[dir]][x + dx[dir]] = 1
                    q.append((y + dy[dir], x + dx[dir]))

color = ['R', 'G', 'B']

res_1 = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(arr[i][j], i, j)
            res_1 += 1
print(res_1, end=' ')

visited = [[0] * n for i in range(n)]

def bfs_1(row, col):
    global visited
    global arr
    q = deque([(row, col)])
    visited[row][col] = 1
    while q:
        (y, x) = q.popleft()
        for dir in range(4):
            if y + dy[dir] < n and y + dy[dir] >= 0 and x + dx[dir] < n and x + dx[dir] >= 0:
                if visited[y + dy[dir]][x + dx[dir]] == 0:
                    if arr[y + dy[dir]][x + dx[dir]] == 'R' or arr[y + dy[dir]][x + dx[dir]] == 'G':
                        visited[y + dy[dir]][x + dx[dir]] = 1
                        q.append((y + dy[dir], x + dx[dir]))
res_1 = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            if arr[i][j] == 'B':
                bfs(arr[i][j], i, j)
            else:
                bfs_1(i, j)
            res_1 += 1
print(res_1)