from collections import deque
a, b = map(int, input().split())

arr = dict()
arr[a] = 0
arr[b] = 0
visited = [a]

q = deque([a])

while q:
    loc = q.popleft()
    for i in range(2):
        if i == 0:
            next_loc = loc * 2
        else:
            next_loc = loc * 10 + 1
        if next_loc > (10**9 + 1):
            break
        if next_loc not in visited:
            q.append(next_loc)
            visited.append(next_loc)
            arr[next_loc] = arr[loc] + 1
        if next_loc == b:
            break
print(arr[b] + 1 if arr[b] != 0 else -1)