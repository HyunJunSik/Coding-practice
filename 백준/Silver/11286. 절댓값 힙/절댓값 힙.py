from heapq import heappush, heappop
import sys

arr = []
for i in range(int(input())):
    n = int(sys.stdin.readline())
    if n != 0:
        heappush(arr, (abs(n), n))
    else:
        if len(arr) == 0:
            print(0)
        else:
            print(heappop(arr)[1])