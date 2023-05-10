n = int(input())
for i in range(1, 1000001):
    num = i
    for j in str(i):
        num += int(j)
    if num == n:
        print(i)
        break
if i == 1000000:
    print(0)