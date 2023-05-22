arr = [i for i in range(1, 31)]
for i in range(28):
    arr.remove(int(input()))
print(min(arr), max(arr), sep='\n')