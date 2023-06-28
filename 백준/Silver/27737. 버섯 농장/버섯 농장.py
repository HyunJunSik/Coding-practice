from collections import deque
n, m, k = map(int, input().split())
visited = [[False] * n for i in range(n)]
arr = [list(map(int, input().split())) for i in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(y, x):
    global visited
    visited[y][x] = True
    q = deque([(y, x)])
    can = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            if can == k:
                return
            n_y, n_x = dy[i] + y, dx[i] + x
            if 0 <= n_y < n and 0 <= n_x < n:
                if not visited[n_y][n_x] and arr[n_y][n_x] == 0:
                    visited[n_y][n_x] = True
                    q.append((n_y, n_x))
                    can += 1
res = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j] and arr[i][j] == 0:
            res += 1
            bfs(i, j)

if m == 0 or res == 0:
    print("IMPOSSIBLE")
elif m - res < 0:
    print("IMPOSSIBLE")
else:
    print("POSSIBLE")
    print(m - res)