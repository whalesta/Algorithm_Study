# 시간초과
N = int(input())
N_list = list(input().split())
M = int(input())
M_list = list(input().split())

for i in M_list:
  if i in N_list:
    print(1)
  else:
    print(0)

## 시간초과2
N = int(input())
N_list = list(input().split())
M = int(input())
M_list = list(input().split())

for i in M_list:
  try:
    N_list.index(i)
    print(1)
  except: print(0)

#####################
# binary search
N = int(input())
N_list = list(input().split())
N_list.sort()

M = int(input())
M_list = list(input().split())


def b_search(target,n_list):
  start_idx = 0
  end_idx = len(n_list)-1
  while start_idx <= end_idx:
      mid_idx = (start_idx + end_idx)//2

      if n_list[mid_idx] > target:
          end_idx = mid_idx - 1
      elif n_list[mid_idx] < target:
          start_idx = mid_idx + 1
      else:
          return mid_idx

  return -1

for m in M_list:
  if b_search(m, N_list)>=0:
    print(1)
  else:
    print(0)