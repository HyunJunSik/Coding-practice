import sys
for c in range(int(input())):
    n = int(input())
    arr = list(map(str, sys.stdin.readline().split()))
    if n > 32:
        print(0)
        continue
    result = 99999
    for i in range(n):
        for j in range(n):
            for k in range(n):
                r = 0
                if i == j or j == k or i == k:
                    continue
                for _ in range(4):
                    if arr[i][_] != arr[j][_]: 
                        r += 1
                    if arr[j][_] != arr[k][_]: 
                        r += 1
                    if arr[i][_] != arr[k][_]: 
                        r += 1             
                result = min(result, r)

    print(result)