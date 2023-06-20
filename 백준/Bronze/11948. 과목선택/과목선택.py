arr = []; m = 0
for i in range(6):
    if i < 4:
        arr.append(int(input()))
    else:
        m = max(m, int(input()))
print(sum(sorted(arr, reverse=True)[:3]) + m)