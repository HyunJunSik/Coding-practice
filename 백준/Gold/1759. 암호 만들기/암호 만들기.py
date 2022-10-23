l, c = map(int, input().split())
arr = sorted(list(map(str, input().split())))


moum = ['a', 'e', 'i', 'o', 'u']
# a c i s t w 
passw = []
def password(passw, cnt, mo, za):
    if cnt == l and len(set(passw)) == l and mo >= 1 and za >= 2:
        print(''.join(passw))
        return
    for i in arr:
        if i in passw:
            continue
        if len(passw) >= 1 and i < passw[cnt -1]:
            continue
        if i in moum:
            passw.append(i)
            password(passw, cnt + 1, mo + 1, za)
            passw.pop()
        else:
            passw.append(i)
            password(passw, cnt + 1, mo, za + 1)
            passw.pop()

password(passw, 0, 0, 0)