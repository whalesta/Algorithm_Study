# 회전하는 큐
import collections
N, M = list(map(int,input().split()))
N_list = [i+1 for i in range(N)]
queue = collections.deque(N_list)

p_list = list(map(int,input().split()))
cnt=0
while len(queue) != (N-M):
  first = queue[0]
  if first == p_list[0]:
    queue.popleft()
    p_list.pop(0)
  else:
    if queue.index(p_list[0])>len(queue)//2:
      last = queue[-1]
      queue.pop()
      queue.appendleft(last)
    else:
      queue.popleft()
      queue.append(first)
    cnt+=1
print(cnt)