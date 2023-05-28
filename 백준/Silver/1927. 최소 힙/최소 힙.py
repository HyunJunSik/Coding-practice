from heapq import heappush, heappop
import sys

arr = []
for i in range(int(sys.stdin.readline())):
    c = int(sys.stdin.readline())
    if c == 0:
        if len(arr) == 0:
            print(0)
        else:
            print(heappop(arr))
    else:
        heappush(arr, c)