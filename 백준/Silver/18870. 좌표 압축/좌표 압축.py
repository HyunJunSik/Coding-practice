n = input();arr = list(map(int, input().split()))
unique = sorted(list(set(arr)))
mapping = {val : i for i, val in enumerate(unique)}
print(*[mapping[val] for val in arr])