N, B = map(int,input().split())
i = 0
NB = []
if N==0:
  NB.append(str(0))
else:
  while N>0:
    n = N%B
    N = N//B
    if n>9:
      NB.append(chr(n+ord('A')-10))
    else:
      NB.append(str(n))

NB.reverse()
print(''.join(NB))