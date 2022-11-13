d = [0] * 1001;

def dp(x):
    if x == 1: 
        return 1
    elif x == 2:
        return 2
    elif d[x] != 0:
        return d[x]
    d[x] = (dp(x-1) + dp(x-2)) % 10007
    return d[x]

x = int(input())
print(dp(x))