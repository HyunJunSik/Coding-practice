result = []
a, b = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(a)]


def riul_1(n, m):
    if m + 2 >= b or n + 1 >= a:
        return
    # 눕혀진 리을 모양
    result.append(arr[n][m] + arr[n][m+1] + arr[n+1][m+1] + arr[n+1][m+2])
    result.append(arr[n][m+1] + arr[n][m+2] + arr[n+1][m] + arr[n+1][m+1])
    # ㅗ, ㅜ 모양
    result.append(arr[n][m] + arr[n][m+1] + arr[n][m + 2] + arr[n+1][m+1])
    result.append(arr[n][m+1] + arr[n+1][m] + arr[n+1][m+1] + arr[n+1][m+2])
    # 눕힌 ㄱ, 대칭 ㄱ 모양
    result.append(arr[n][m] + arr[n][m+1] + arr[n][m+2] + arr[n+1][m])
    result.append(arr[n][m] + arr[n][m+1] + arr[n][m+2] + arr[n+1][m+2])
    # 눕힌 ㄱ, 대칭 ㄱ 모양(180도 회전)
    result.append(arr[n][m+2] + arr[n+1][m] + arr[n+1][m+1] + arr[n+1][m+2])
    result.append(arr[n][m] + arr[n+1][m] + arr[n+1][m+1] + arr[n+1][m+2])
    return


def riul_2(n, m):
    if m + 1 >= b or n + 2 >= a:
        return
    # 세워진 리을 모양
    result.append(arr[n][m+1] + arr[n+1][m+1] + arr[n+1][m] + arr[n+2][m])
    result.append(arr[n][m] + arr[n+1][m] + arr[n+1][m+1] + arr[n+2][m+1])
    # ㅏ,ㅓ 모양
    result.append(arr[n][m] + arr[n+1][m] + arr[n+2][m] + arr[n+1][m+1])
    result.append(arr[n][m+1] + arr[n+1][m+1] + arr[n+1][m] + arr[n+2][m+1])
    # 세워진 ㄱ, 대칭 ㄱ 모양
    result.append(arr[n][m] + arr[n][m+1] + arr[n+1][m] + arr[n+2][m])
    result.append(arr[n][m] + arr[n][m+1] + arr[n+1][m+1] + arr[n+2][m+1])
    # 세워진 ㄴ, 대칭 ㄴ 모양
    result.append(arr[n][m] + arr[n+1][m] + arr[n+2][m] + arr[n+2][m+1])
    result.append(arr[n][m+1] + arr[n+1][m+1] + arr[n+2][m+1] + arr[n+2][m])
    return

def sq(n, m):
    # 정사각형 모양
    if m + 1 >= b or n + 1 >= a:
        return
    result.append(arr[n][m] + arr[n+1][m] + arr[n][m+1] + arr[n+1][m+1])
    return


def li_1(n, m):
    # 세워진 1자 모양
    if m >= b or n + 3 >= a:
        return
    result.append(arr[n][m] + arr[n+1][m] + arr[n+2][m] + arr[n+3][m])
    return


def li_2(n, m):
    # 눕혀진 1자 모양
    if m + 3 >= b or n >= a:
        return
    result.append(arr[n][m] + arr[n][m + 1] + arr[n][m + 2] + arr[n][m + 3])
    return


for i in range(a):
    for j in range(b):
        # 주어진 종이의 칸 수를 이중 for문으로 시작점을 i, j로 두고 각 함수에 모두 대입
        # 각 함수 조건에 따라 테트로미노가 놓인 칸에 쓰인 수들의 합을 구할 것임
        riul_1(i, j)
        riul_2(i, j)
        sq(i, j)
        li_1(i, j)
        li_2(i, j)
print(max(result))