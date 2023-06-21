from collections import deque
m,n,k = map(int, input().split())
visited = [[False] * n for i in range(m)] 

def bfs(y, x):
    global visited
    res = 1
    visited[y][x] = True
    q = deque([(y, x)])

    while q:
        y, x = q.popleft()
        for i in range(4):
            dx, dy = x + n_x[i], y + n_y[i]
            if dx >= 0 and dx < n and dy >= 0 and dy < m:
                if not visited[dy][dx]:
                    res += 1
                    q.append((dy, dx))
                    visited[dy][dx] = True
    return res


for i in range(k):
    dx, dy, ux, uy = map(int, input().split())
    for x in range(dx, ux):
        for y in range(m - uy, m - dy):
            visited[y][x] = True

result = []
n_x = [0, 0, 1, -1]
n_y = [1, -1, 0, 0]

for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            result.append(bfs(i, j))
print(len(result))
print(*sorted(result))
