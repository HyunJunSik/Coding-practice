from collections import deque
n, m = map(int, input().split())
M = [list(input()) for i in range(m)]
visited = [[False] * n for i in range(m)]

def bfs(y, x, c):
    global visited
    cnt = 1
    q = deque([(y, x)])
    visited[y][x] = True

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    while q:
        y, x = q.popleft()
        for i in range(4):
            n_y, n_x = dy[i] + y, dx[i] + x
            if 0 <= n_y < m and 0 <= n_x < n:
                if not visited[n_y][n_x] and M[n_y][n_x] == c:
                    q.append((n_y, n_x))
                    visited[n_y][n_x] = True
                    cnt += 1
    return cnt ** 2

w = 0
b = 0
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            if M[i][j] == 'W':
                w += bfs(i, j, 'W')
            else:
                b += bfs(i, j, 'B')
print(w, b)