N = 1000 - int(input())
wallet = [500, 100, 50, 10, 5, 1]
cnt, i = 0, 0

while N>0:
  if wallet[i] <= N:
    cnt+=1
    N = N-wallet[i]
  else:
    i+=1

print(cnt)