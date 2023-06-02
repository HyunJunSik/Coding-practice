n, m = map(int, input().split())

answer = []
def b(depth):
    if depth == m:
        print(*answer)
        return
    for i in range(1, n + 1):
        if len(answer) > 0:
            if answer[-1] > i:
                continue
        answer.append(i)
        b(depth + 1)
        answer.pop()
b(0)