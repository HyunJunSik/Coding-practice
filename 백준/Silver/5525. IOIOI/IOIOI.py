n=int(input());p='I'+'OI'*n;m = int(input());S = input()
result = 0
for i in range(m - 2 * n):
    if S[i: (2*n+1+i)] == p:
        result += 1
print(result)