chess1 = [
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW'
    ]
chess2 = [
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    ]
n, m = map(int, input().split())
arr = [input() for i in range(n)]
result = []
for y in range(n - 7):
    for x in range(m - 7):
        cnt = 0
        for line in range(8):
            check = arr[line + y][x : 8 + x]
            if check != chess1[line]:
                for lines in range(8):
                    if chess1[line][lines] != check[lines]:
                        cnt += 1
        result.append(cnt)
        cnt = 0
        for line in range(8):
            check = arr[line + y][x : 8 + x]
            if check != chess2[line]:
                for lines in range(8):
                    if chess2[line][lines] != check[lines]:
                        cnt += 1
        result.append(cnt)
print(min(result))