from collections import deque

n,m = map(int, input().split())
maze = [list(map(int, input())) for i in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if next_x >= 0 and next_x < m and next_y >= 0 and next_y < n:
                if maze[next_y][next_x] == 1:
                    maze[next_y][next_x] = maze[y][x] + 1
                    q.append((next_x, next_y))
    return maze[n-1][m-1]

print(bfs(0,0))

