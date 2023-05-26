for i in range(int(input())):
    d = {}
    for j in range(int(input())):
        w, type = map(str, input().split())
        if type in d:
            d[type] += 1
        else:
            d[type] = 1
    result = 1
    for t in d.values():
        result *= t + 1
    print(result - 1)