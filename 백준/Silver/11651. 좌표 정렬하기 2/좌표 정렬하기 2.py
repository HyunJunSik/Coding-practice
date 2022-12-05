def Ex11651():
    arr = []
    for i in range(int(input())):
        x, y = map(int, input().split())
        arr.append((x,y))
    arr.sort(key=lambda x: x[0])
    arr.sort(key=lambda x: x[1])
    for i in arr:
        print(i[0], i[1])
Ex11651()