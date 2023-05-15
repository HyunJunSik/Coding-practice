n, m = map(int, input().split())
arr1 = set(input() for i in range(n))
arr2 = set(input() for i in range(m))
result = sorted(set.intersection(arr1, arr2))
print(len(result))
for name in result:
    print(name)