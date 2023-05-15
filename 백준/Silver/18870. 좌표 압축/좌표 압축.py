n=input();a=list(map(int, input().split()))
u=sorted(list(set(a)))
m={v:i for i,v in enumerate(u)}
print(*[m[v] for v in a])