from collections import Counter
arr = []
for i in range(int(input())):
    arr.append(int(input()))
arr = sorted(arr)
counter  = Counter(arr).most_common(2)
print(round(sum(arr) / len(arr)))
print(arr[int(len(arr)/2)])
if len(counter) > 1:
    print(counter[0][0] if counter[0][1] != counter[1][1] else counter[1][0])
else:
    print(counter[0][0])
print(arr[-1] - arr[0])