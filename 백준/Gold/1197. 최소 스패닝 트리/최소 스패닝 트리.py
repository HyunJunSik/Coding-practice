v, e=  map(int, input().split())
arr = []
for i in range(e):
    a, b, cost = map(int, input().split())
    arr.append((cost, a, b))
arr.sort()

parent = list(range(v+1))

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x] 

def merge(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

total = 0

for i in arr:
    cost, a, b = i
    if find_parent(parent, a) != find_parent(parent, b):
        merge(parent, a, b)
        total += cost
print(total)
