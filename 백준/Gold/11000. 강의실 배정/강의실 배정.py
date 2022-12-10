def Ex11000():
    import heapq
    time = []
    for i in range(int(input())):
        s, e = map(int, input().split())
        heapq.heappush(time, (s, e))
    time.sort(key = lambda x : x[0])
    c = []
    heapq.heappush(c, time[0][1])
    for i in range(1, len(time)):
        if time[i][0] >= c[0]:
            heapq.heappop(c)
        heapq.heappush(c, time[i][1])
    print(len(c))
Ex11000()