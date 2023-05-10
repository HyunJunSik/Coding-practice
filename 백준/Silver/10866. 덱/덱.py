import sys

def d(D, com):
    if com[0] == 'push_front':
        D.append(int(com[1]))
    elif com[0] == 'push_back':
        D.insert(0, int(com[1]))
    elif com[0] == 'pop_front':
        if len(D) == 0:
            print(-1)
        else:
            print(D.pop())
    elif com[0] == 'pop_back':
        if len(D) == 0:
            print(-1)
        else:
            n = D[0]
            del D[0]
            print(n)
    elif com[0] == 'size':
        print(len(D))
    elif com[0] == 'empty':
        if len(D) == 0:
            print(1)
        else:
            print(0)
    elif com[0] == 'front':
        if len(D) == 0:
            print(-1)
        else:
            print(D[-1])
    elif com[0] == 'back':
        if len(D) == 0:
            print(-1)
        else:
            print(D[0])
    return D

D = []
for i in range(int(input())):
    D = d(D, sys.stdin.readline().split())
    