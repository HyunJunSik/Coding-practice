n, l = map(int, input().split())
h = sorted(list(map(int, input().split())))
for fruit in h:
    if l >= fruit:
        l = l + 1
    else:
        break
print(l)