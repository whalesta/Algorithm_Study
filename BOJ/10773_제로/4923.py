# 문제 (단계/자료구조)
# 나코더 기장 재민이는 동아리 회식을 준비하기 위해서 장부를 관리하는 중이다.
# 재현이는 재민이를 도와서 돈을 관리하는 중인데, 애석하게도 항상 정신없는 재현이는 돈을 실수로 잘못 부르는 사고를 치기 일쑤였다.
# 재현이는 잘못된 수를 부를 때마다 0을 외쳐서, 가장 최근에 재민이가 쓴 수를 지우게 시킨다.
# 재민이는 이렇게 모든 수를 받아 적은 후 그 수의 합을 알고 싶어 한다. 재민이를 도와주자!

# 입력
# 첫 번째 줄에 정수 K가 주어진다. (1 ≤ K ≤ 100,000)
# 이후 K개의 줄에 정수가 1개씩 주어진다. 정수는 0에서 1,000,000 사이의 값을 가지며, 정수가 "0" 일 경우에는 가장 최근에 쓴 수를 지우고, 아닐 경우 해당 수를 쓴다.
# 정수가 "0"일 경우에 지울 수 있는 수가 있음을 보장할 수 있다.

# 출력
# 재민이가 최종적으로 적어 낸 수의 합을 출력한다. 최종적으로 적어낸 수의 합은 2^31-1보다 작거나 같은 정수이다.

# ---

# 최근의 값이 빠지므로 LIFO의 stack 자료구조 문제다. 리스트의 pop과 append를 사용하면 된다. I/O: O(1)
# 출력은 int type이라는 말이다. 파이썬은 int로 표현할 수 있는 최대치를 넘기면 자동으로 long 변환되니 무시할 것.

# --
import sys

def write_down(K:int, note:list) -> list:
    for _ in range(K):
        number = int(sys.stdin.readline())
        if number != 0:
            note.append(number)
        else:
            note.pop()
    return note

def main():
    # Input
    K = int(sys.stdin.readline())
    note = list()

    # write down
    final_note:list = write_down(K, note)

    # output
    return sum(final_note)

if __name__ == "__main__":
    print(main())