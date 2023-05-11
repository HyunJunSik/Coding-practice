ans = ['a','b','c','d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n','o','p','q','r','s','t','u','v','w','x','y','z']
cnt = 0
n = int(input())
arr = input()
for i in range(n):
    cnt += (ans.index(arr[i]) + 1) * (31**i)
print(cnt % 1234567891)