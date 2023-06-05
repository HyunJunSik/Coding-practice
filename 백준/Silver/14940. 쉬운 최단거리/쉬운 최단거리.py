from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
result = [[-1] * m for i in range(n)]
visited = [[False] * m for i in range(n)]

dx = [0, 0, -1 , 1]
dy = [1, -1, 0, 0]

def bfs(y, x):
    global visited
    global result
    q = deque([(y, x)])
    while q:
        (y, x) = q.popleft()
        for k in range(4):
            next_y = dy[k] + y
            next_x = dx[k] + x
            if next_y >= 0 and next_y < n and next_x >= 0 and next_x < m:
                if arr[next_y][next_x] == 1 and visited[next_y][next_x] == False:
                    visited[next_y][next_x] = True
                    result[next_y][next_x] = result[y][x] + 1
                    q.append((next_y, next_x))
    return

goal = (0, 0)
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            goal = (i, j)
            result[i][j] = 0
            break

bfs(goal[0], goal[1])

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            result[i][j] = 0
                
for i in range(n):
    print(*result[i])