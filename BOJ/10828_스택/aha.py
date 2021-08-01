class Stack():
  def __init__(self):
    self.stack=[]

  def push(self,num):
    self.stack.append(int(num))

  def pop(self):
    if self.empty()==1:
        return -1
    else:
        return self.stack.pop(-1)

  def size(self):
      return len(self.stack)

  def empty(self):
      if self.size()==0:
          return 1
      else:
          return 0

  def top(self):
      if self.empty()==1:
          return -1
      else:
          return self.stack[-1]

def run_stack(s,textnum):
  text=textnum[0]
  if text=='push':
    _, num=text
    s.push(int(num))
  elif text=='pop':
      print(s.pop())
  elif text=='top':
      print(s.top())
  elif text == 'size':
      print(s.size())
  elif text == 'empty':
      print(s.empty())
  return s


N=int(input())
ST=Stack()
for i in range(N):
  textnum=input().split()
  run_stack(ST,textnum)
