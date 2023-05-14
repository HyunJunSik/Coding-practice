N, r, c = map(int, input().split())
result = 0
def recursive(N, r, c):
    
    global result
    if N == -1:
        return
    N -= 1 
    if r // (2**N) == 0 and c // (2**N) == 0:
        result += 0
    elif r // (2**N) == 0 and c // (2**N) == 1:
        result += (2**N)**2
        c -= (2**N)
    elif r // (2**N) == 1 and c // (2**N) == 0:
        result += (2**N)**2 * 2
        r -= (2**N)
    else:
        result += (2**N)**2 * 3
        c -= (2**N)
        r -= (2**N)
    recursive(N, r, c)

recursive(N, r, c)
print(result)