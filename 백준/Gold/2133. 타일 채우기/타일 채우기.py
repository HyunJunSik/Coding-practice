d = [0] * 1001;

def dp(x):
    if x == 0:
        return 1;
    if x== 1:
        return 0
    elif x == 2:
        return 3
    elif d[x] != 0:
        return d[x]
    result = 3 * dp(x - 2)
    for i in range(3, x + 1):
        if x % 2 == 0:
            result += 2 * dp(x-i)
    d[x] = result
    return d[x]

x = int(input())
print(dp(x))