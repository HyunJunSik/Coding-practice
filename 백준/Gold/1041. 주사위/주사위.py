n=int(input())
a,b,c,d,e,f = map(int,input().split())
one = min(a,b,c,d,e,f)
two = min(a+b,a+c,a+e,a+d,c+b,b+d,d+e,e+c,f+c,f+b,f+d,f+e)
three = min(a+b+c,a+b+d,a+d+e,a+c+e,f+e+c,f+d+e,f+b+d,f+b+c)
if n > 1:
    print((n-2)**2*one+(n-1)*(n-2)*4*one+4*three+(2*n-3)*4*two)
else:
    sum = a+b+c+d+e+f-max(a,b,c,d,e,f)
    print(sum)