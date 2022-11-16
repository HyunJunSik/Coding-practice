n = input().split('-')
n[0] = n[0].split('+')
result = sum([int(i) for i in n[0]])
for i in range(1, len(n)):
    n[i] = n[i].split('+')
    result -= sum([int(j) for j in n[i]])
print(result)