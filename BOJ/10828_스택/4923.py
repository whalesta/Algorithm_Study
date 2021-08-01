# 스택 구현 문제

import sys


class Stack:
    def __init__(self):
        self.array = [None for _ in range(5)]
        self.array_size = 0

    def push(self, num):
        self.array.append(num)
        self.array_size += 1

    def pop(self):
        if self.array_size == 0:
            return -1
        self.array_size -= 1
        return self.array.pop()

    def size(self):
        return self.array_size

    def empty(self):
        if self.array_size == 0:
            return 1
        return 0

    def top(self):
        if self.array_size == 0:
            return -1
        return self.array[-1]


def main():
    # 최대 10000개의 명령을 입력받게 되므로 sys
    N = int(sys.stdin.readline().strip())

    # Stack 생성
    S = Stack()
    for _ in range(N):
        commands = sys.stdin.readline().strip().split()
        command = commands[0]

        if command == "push":
            S.push(commands[1])
        elif command == "pop":
            stack_pop = S.pop()
            print(stack_pop)
        elif command == "size":
            stack_size = S.size()
            print(stack_size)
        elif command == "empty":
            stack_empty = S.empty()
            print(stack_empty)
        elif command == "top":
            stack_top = S.top()
            print(stack_top)


if __name__ == "__main__":
    main()
