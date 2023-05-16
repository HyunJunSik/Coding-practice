import sys
def s(S, com):
    c = com[0]
    if c == "add":
        S.add(int(com[1]))
        return S
    elif c == "remove":
        S.discard(int(com[1]))
        return S
    elif c == "check":
        if int(com[1]) in S:
            print(1)
        else:
            print(0)
        return S
    elif c == "toggle":
        if S.isdisjoint({int(com[1])}):
            S.add(int(com[1]))
            return S
        else:
            S.discard(int(com[1]))
            return S
    elif c == "all":
        return {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
    else:
        return set()
S = set()
for i in range(int(input())):
    S = s(S, sys.stdin.readline().split())