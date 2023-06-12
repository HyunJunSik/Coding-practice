import sys
a,b,c = map(int, sys.stdin.readline().split())
def f(a, b):
    if b == 1:
        return a % c
    x = f(a, b // 2)
    if b % 2 == 0:
        return x * x % c
    else:
        return x * x * a % c
print(f(a, b))