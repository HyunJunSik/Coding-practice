n = int(input())
arr = [input().strip() for i in range(n)]

def f(n, arr):
    
    if arr == ['1'*n for i in range(n)]:
        return '1'
    elif arr == ['0'*n for i in range(n)]:
        return '0'
    
    arr1 = [arr[i][:(n//2)] for i in range(n//2)]
    arr2 = [arr[i][(n//2):] for i in range(n//2)]
    arr3 = [arr[i + n//2][:(n//2)] for i in range(n//2)]
    arr4 = [arr[i + n//2][(n//2):] for i in range(n//2)]
    return '(' + f(n//2, arr1) + f(n//2, arr2) + f(n//2, arr3) + f(n//2, arr4) + ')'
print(f(n, arr))