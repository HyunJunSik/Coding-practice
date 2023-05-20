a, b = map(int, input().split())
A = []
B = []
for i in range(a):
    A.append(list(map(int, input().split())))
for i in range(a):
    B.append(list(map(int, input().split())))
for i in range(a):
    for j in range(b):
        print(A[i][j] + B[i][j], end=' ')
    print()