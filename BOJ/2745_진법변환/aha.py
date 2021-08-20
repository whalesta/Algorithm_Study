## 1
N, B = input().split()
B = int(B)
N = list(N)
total = 0
j = -1

for i in range(len(N)):
  if N[j].isdigit()==True:
    idx = int(N[j])
  else:
    idx = ord(N[j]) - ord('A') + 10
  j -= 1
  total += idx*B**i
print(total)


## 2
N, B = input().split()
B = int(B)
N = list(N)
total = 0
j = -1
i = 0

def rec(N, B, i, j, total):
  if i >=len(N):
    return total
  elif N[j].isdigit() == True:
    idx=int(N[j])
  else:
    idx = ord(N[j]) - ord('A') + 10
  total += idx*B**i
  return rec(N, B, i+1, j-1, total)

print(rec(N, B, i, j, total))