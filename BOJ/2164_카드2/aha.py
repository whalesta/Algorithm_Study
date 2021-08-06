N = int(input())
N_list = [i+1 for i in range(N)]
while len(N_list)>0:
  first = N_list[0]
  N_list.pop(0)
  if len(N_list)==0:
    print(first)
  else:
    two = N_list[0]
    N_list.pop(0)
    N_list.append(two)