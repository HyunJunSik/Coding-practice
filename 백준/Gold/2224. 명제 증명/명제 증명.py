Inf = int(1e9)
arr = []
alpha = []
x = int(input())
for i in range(x):
    a = input().split()
    arr.append((a[0],a[2]))
    alpha.append(a[0])
    alpha.append(a[2])
alpha = sorted(list(set(alpha)))
diction = {}
n = len(alpha)
for i in range(n):
    diction[alpha[i]] = i
graph = [[Inf] * n for i in range(n)]
for i in range(x):
    u, v = diction[arr[i][0]], diction[arr[i][1]]
    graph[u][v] = 1

for i in range(n):
    for j in range(n):
        if i == j:
            graph[i][j] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])


ans = []
cnt = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] < Inf and graph[i][j] > 0:
            a, b = '',''
            for key, value in diction.items():
                if value == i:
                    a = key
                    break
            for key, value in diction.items():
                if value == j:
                    b = key
                    break
            cnt += 1
            ans.append((a,b))
print(cnt)
for i in ans:
    print(i[0] + " => "+i[1])