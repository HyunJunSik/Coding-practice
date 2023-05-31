from collections import deque
n = int(input())
arr = [input() for i in range(n)]
visited = [[False] * n for i in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
result = []
def bfs(y, x):
    global arr
    global visited
    cnt = 1
    q = deque([(y, x)])
    visited[y][x] = True
    while q:
        y, x = q.popleft()
        for i in range(4):
            if dx[i] + x >= 0 and dx[i] + x < n and dy[i] + y >= 0 and dy[i] + y < n:
                if visited[dy[i] + y][dx[i] + x] == False and arr[dy[i] + y][dx[i] + x] == '1':
                    visited[dy[i] + y][dx[i] + x] = True
                    q.append((dy[i] + y, dx[i] + x))
                    cnt += 1
    return cnt

for i in range(n):
    for j in range(n):
        if visited[i][j] == False and arr[i][j] == '1':
            result.append(bfs(i, j))
print(len(result))
for i in sorted(result):
    print(i)