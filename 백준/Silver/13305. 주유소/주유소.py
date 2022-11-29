n = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))
cost.pop()
cost_sort = sorted(cost)
visit = [0] * len(cost)
result = 0
for i in cost_sort:
    if visit[cost.index(i)] == 0:
        for j in range(cost.index(i), len(cost)):
            if visit[j] == 1:
                break
            visit[j] = 1
            result += cost[cost.index(i)] * dist[j]
print(result)