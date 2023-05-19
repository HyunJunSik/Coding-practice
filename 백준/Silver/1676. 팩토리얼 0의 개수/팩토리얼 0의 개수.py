def f(num):
    if num == 0:
        return 1
    if num == 1:
        return 1
    return num * f(num - 1)
n = str(f(int(input())))
cnt = 0
for i in range(len(n) - 1, -1, -1):
    if n[i] != '0':
        break
    cnt += 1
print(cnt)