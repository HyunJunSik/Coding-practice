import heapq
Inf = int(1e9)

n = int(input())
m = int(input())
distance = [Inf] * (n + 1)

visited = [False] * (n + 1)
graph = [[] for i in range(n+1)]

for _ in range(m):
  u, v = map(int, input().split())
  graph[u].append((v, 1))
  graph[v].append((u, 1))
def d(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:
    dist, u = heapq.heappop(q)
    if distance[u] < dist:
      continue
    for i in graph[u]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]]= cost
        heapq.heappush(q, (cost, i[0]))
d(1)
cnt = 0
for i in range(2, n + 1):
  if distance[i] != Inf:
    cnt += 1
print(cnt)