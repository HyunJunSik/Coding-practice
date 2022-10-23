from collections import deque

m, n = map(int ,input().split())
arr = [list(map(int, input().split())) for i in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]
q = deque()
for i in range(m):
    for j in range(n):
        if arr[j][i] == 1:
            q.append((i, j))

while q:            
    i, j = q.popleft()
    for k in range(4):
        new_x = i + dx[k]
        new_y = j + dy[k]
        if new_x >= 0 and new_x < m and new_y >= 0 and new_y < n:
            if arr[new_y][new_x] == 0:
                arr[new_y][new_x] = arr[j][i] + 1
                q.append((new_x, new_y))
result = 0
for i in arr:
    if result < max(i):
        result = max(i)
    if 0 in i:
        result = 0
        break  
print(result - 1)