N, M = map(int, input().split())
res = [input() for i in range(N)]
que = [input() for i in range(M)]
res.insert(0, '')
for q in que:
    try: print(res[int(q)])
    except: print(res.index(q))