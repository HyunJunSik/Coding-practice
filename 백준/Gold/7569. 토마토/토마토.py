from collections import deque
def bfs(q):
    global visited
    global arr
    while q:
        (x, y, z) = q.popleft()
        for i in range(4):
            next_x = x + move_x[i]
            next_y = y + move_y[i]
            if next_x >= 0 and next_x < m and next_y >= 0 and next_y < n:
                if not visited[z][next_y][next_x] and arr[z][next_y][next_x] == 0:
                    q.append((next_x, next_y, z))
                    visited[z][next_y][next_x] = True
                    arr[z][next_y][next_x] = arr[z][y][x] + 1
        for i in range(2):
            next_z = z + move_z[i]
            if next_z >= 0 and next_z < h:
                if not visited[next_z][y][x] and arr[next_z][y][x] == 0:
                    q.append((x, y, next_z))
                    visited[next_z][y][x] = True
                    arr[next_z][y][x] = arr[z][y][x] + 1


m, n, h = map(int, input().split())
arr = [[list(map(int, input().split())) for i in range(n)] for j in range(h)]
visited = [[[False] * m for i in range(n)] for j in range(h)]

flag = False
move_x = [0, 0, 1, -1]
move_y = [1, -1, 0, 0]
move_z = [1, -1]

for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 0:
                flag = True
                break
if flag == True:
    q = deque([])
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if arr[i][j][k] == 1:
                    visited[i][j][k] = True
                    q.append((k, j, i))
    bfs(q)
    flag = False
    res = 0
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if arr[i][j][k] == 0:
                    flag = True
                    break
                else:
                    res = max(res, arr[i][j][k])

    print(-1 if flag == True else res - 1)
else:
    print(0)