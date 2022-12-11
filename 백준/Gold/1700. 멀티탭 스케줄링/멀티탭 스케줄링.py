def Ex1700():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    plug = [arr[0]]
    result = 0
    for i in range(1, k):
        if len(plug) < n and arr[i] not in plug:
            plug.append(arr[i])
        if len(plug) == n and arr[i] not in plug:
            c = [k + 1] * n
            for j in range(n):
                for m in range(i, k):
                    if plug[j] == arr[m]:
                        c[j] = min(c[j], m)
            del plug[c.index(max(c))]
            result += 1
            plug.append(arr[i])
    print(result)
Ex1700()