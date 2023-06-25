n = int(input())
while True:
    num = int(input())
    if num == 0:
        break
    print(str(num) + " is a multiple of " + str(n) + "." if not num % n  else str(num) + " is NOT a multiple of " + str(n) + ".")