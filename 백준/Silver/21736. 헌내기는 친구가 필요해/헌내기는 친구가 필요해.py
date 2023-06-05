from collections import deque
n,m = map(int, input().split())
arr = [list(input()) for i in range(n)]
v = [[False] * m for i in range(n)]
goal = (0, 0)
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'I':
            goal = (i, j)     
def bfs(y, x):
    global v
    result = 0
    q = deque([(y, x)])
    while q:
        (y, x) = q.popleft()
        for i in range(4):
            n_y = y + dy[i]
            n_x = x + dx[i]
            if n_y >= 0 and n_y < n and n_x >= 0 and n_x < m:
                if arr[n_y][n_x] == 'O' and not v[n_y][n_x]:
                    v[n_y][n_x] = True
                    q.append((n_y, n_x))
                elif arr[n_y][n_x] == 'P' and not v[n_y][n_x]:
                    result += 1
                    v[n_y][n_x] = True
                    q.append((n_y, n_x))
    return result
result = bfs(goal[0], goal[1])
print(result if result > 0 else "TT")
