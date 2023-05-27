from collections import deque
for i in range(int(input())):
    flag = False
    rev_cnt = 0
    c = list(input().strip())
    length = int(input())
    num = input()
    if num == "[]":
        q = deque([])
    else:
        q = deque(num[1:-1].split(","))
    for j in c:
        if j == 'R':
            rev_cnt += 1
        else:
            if len(q) > 0:
                if rev_cnt % 2 == 0:
                    q.popleft()
                else:
                    q.pop()
            else:
                print("error")
                flag = True
                break
    if flag == False:
        if rev_cnt % 2 == 0:
            print("[",end="")
            print(','.join(q),end="")
            print("]")
        else:
            q.reverse()
            print("[",end="")
            print(','.join(q),end="")
            print("]")