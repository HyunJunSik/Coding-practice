from collections import deque
import sys
# 1 : D, 2 : S, 3 : L, 4 : R
for i in range(int(sys.stdin.readline())):
    A, B = map(int, sys.stdin.readline().split())
    visited = [False] * 10000
    q = deque([(A, "")])
    while q:
        num, path = q.popleft()
        if num == B:
            print(path)
            break
        # case D
        n_num = num * 2
        if n_num > 9999:
            n_num %= 10000
        if not visited[n_num]:
            visited[n_num] = True
            q.append((n_num, path+"D"))
        # case S
        if num == 0:
            n_num = 9999
        else:
            n_num = num - 1
        if not visited[n_num]:
            visited[n_num] = True
            q.append((n_num, path+"S"))
        # case L
        left = num // 1000
        right = num % 1000
        n_num = right * 10 + left
        if not visited[n_num]:
            visited[n_num] = True
            q.append((n_num, path+"L"))
        # case R
        left = num // 10
        right = num % 10
        n_num = right * 1000 + left
        if not visited[n_num]:
            visited[n_num] = True
            q.append((n_num, path+"R"))
    
        
