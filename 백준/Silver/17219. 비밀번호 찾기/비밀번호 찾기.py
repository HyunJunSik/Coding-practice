d = dict()
n,m = map(int, input().split())
for i in range(n):
    addr, passwd = map(str, input().split())
    d[addr] = passwd
ans = []
for i in range(m):
    ans.append(d[input()])
for i in ans:
    print(i)