def check(sentence):
  arr = []
  for pos in sentence:
    for c in pos:
      if '[' == c:
        arr.append(c)
      elif ']' == c:
        if len(arr) == 0:
          return 0
        bal = arr.pop()
        if bal != '[':
          return 0

      elif '(' == c:
        arr.append(c)
      elif ')' == c:
        if len(arr) == 0:
          return 0
        bal = arr.pop()
        if bal != '(':
          return 0
  if len(arr) == 0:
    return 1
  else:
    return 0


while True:
  n = input()
  if n == ".":
    break
  n = n.split()
  if check(n) == 1:
    print("yes")
  else:
    print("no")
  