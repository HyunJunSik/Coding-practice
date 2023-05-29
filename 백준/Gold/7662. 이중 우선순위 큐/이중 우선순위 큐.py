import sys
from heapq import heappush, heappop

for i in range(int(input())):
    h_max = []
    h_min = []
    k = int(input())
    visited = [False] * k
    for j in range(k):
        com, num = map(str, sys.stdin.readline().split())
        if com == 'I':
            heappush(h_max, (-1 * int(num), j))
            heappush(h_min, (int(num), j))
            visited[j] = True
        else:
            if num == '1':
                while h_max and not visited[h_max[0][1]]:
                    heappop(h_max)
                if h_max:
                    visited[h_max[0][1]] = False
                    heappop(h_max)
            else:
                while h_min and not visited[h_min[0][1]]:
                    heappop(h_min)
                if h_min:
                    visited[h_min[0][1]] = False
                    heappop(h_min)
    while h_max and not visited[h_max[0][1]]:
        heappop(h_max)
    while h_min and not visited[h_min[0][1]]:
        heappop(h_min)
    if h_max:
        print(-1 * h_max[0][0], h_min[0][0])
    else:
        print("EMPTY")
