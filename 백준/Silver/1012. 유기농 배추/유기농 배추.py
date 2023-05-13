from collections import deque
global visited, M, N
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(arr, visited, y, x):
    q = deque()
    q.append((x, y))
    visited[y][x] = 1

    while q:
        (x, y) = q.popleft()
        for i in range(4):
            if x + dx[i] >= 0 and x + dx[i] < M and y + dy[i] >= 0 and y + dy[i] < N:
                if arr[y + dy[i]][x + dx[i]] == 1 and visited[y + dy[i]][x + dx[i]] == 0:
                    q.append((x + dx[i], y + dy[i]))
                    visited[y + dy[i]][x + dx[i]] = 1

for i in range(int(input())):
    M, N, K = map(int, input().split())
    arr = [[0] * M for j in range(N)]
    visited = [[0] * M for j in range(N)]
    for j in range(K):
        X, Y = map(int, input().split())
        arr[Y][X] = 1
    cnt = 0
    for j in range(M):
        for k in range(N):
            if arr[k][j] == 1 and visited[k][j] == 0:
                # 방문하지 않은 무
                cnt += 1
                bfs(arr, visited, k, j)
    print(cnt)
    
    