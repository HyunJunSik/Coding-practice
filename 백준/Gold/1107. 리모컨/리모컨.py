N = int(input()) ; M = int(input())
if M == 0:
    K = []
else:
    K = list(map(int, input().split()))

result = abs(100 - N)

for i in range(1000001):
    num = str(i)
    for j in range(len(num)):
        if int(num[j]) in K:
            break
        elif j == len(num) - 1:
            result = min(result, abs(int(num) - N) + len(num))
print(result)