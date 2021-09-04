# 문제
# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 
# 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 
# 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 
# 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 
# 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 
# 모든 정수의 범위는 -2^31 보다 크거나 같고 2^31보다 작다.

# 출력
# M개의 줄에 답을 출력한다. 
# 존재하면 1을, 존재하지 않으면 0을 출력한다.

# ---
# 빠른 탐색이 key : 어떻게?
# ---

import sys

def binary_search(target:int, find:list):
    half = len(find)//2

    print(f"\t\t[recursion] 'find' list is [{find}]\t => \t {find[half]}")

    # return
    if target == find[half]:    # find!
        print("*"*5 + " FIND! ", "*"*5, "=> ", find[half])
        return 1
    elif len(find) == 1:   # break condition
        return 0
    
    # search
    if target <= find[half]:
        new_find = find[:half]
        binary_search(target, new_find)  # new list
    else:
        new_find = find[half:]
        binary_search(target, new_find) # new list



def main():
    # input 1: search_numbers
    N = int(sys.stdin.readline().strip())
    search_numbers = map(int, input().split(" "))

    # input 2: target_numbers to find
    M = int(sys.stdin.readline().strip())
    target_numbers = map(int, input().split(" "))
    sorted_list = sorted(search_numbers)

    # output
    result_list = list()
    for target in target_numbers:
        print(f"target number is **{target}**, sorted_list is [{sorted_list}]")
        print(binary_search(target, sorted_list))
        result_list.append(binary_search(target, sorted_list))

        print(f"\tresult_list is [{result_list}]")
        print("="*20)

    # for number in result:    # constructed 0 or 1, len(result_list) = M
    #     print(number)
    return

if __name__ == "__main__":
    main()

# ===============================================
# 아니 이해가 안되네

# 5
# 4 1 5 2 3
# 5
# 1 3 7 9 5
# target number is **1**, sorted_list is [[1, 2, 3, 4, 5]]
#                 [recursion] 'find' list is [[1, 2, 3, 4, 5]]     =>      3
#                 [recursion] 'find' list is [[1, 2]]      =>      2
#                 [recursion] 'find' list is [[1]]         =>      1
# ***** FIND!  ***** =>  1
# None
#                 [recursion] 'find' list is [[1, 2, 3, 4, 5]]     =>      3
#                 [recursion] 'find' list is [[1, 2]]      =>      2
#                 [recursion] 'find' list is [[1]]         =>      1
# ***** FIND!  ***** =>  1
#         result_list is [[None]]
# ====================
# target number is **3**, sorted_list is [[1, 2, 3, 4, 5]]
#                 [recursion] 'find' list is [[1, 2, 3, 4, 5]]     =>      3
# ***** FIND!  ***** =>  3
# 1
#                 [recursion] 'find' list is [[1, 2, 3, 4, 5]]     =>      3
# ***** FIND!  ***** =>  3
#         result_list is [[None, 1]]
# ====================
# target number is **7**, sorted_list is [[1, 2, 3, 4, 5]]
#                 [recursion] 'find' list is [[1, 2, 3, 4, 5]]     =>      3
#                 [recursion] 'find' list is [[3, 4, 5]]   =>      4
#                 [recursion] 'find' list is [[4, 5]]      =>      5
#                 [recursion] 'find' list is [[5]]         =>      5
# None
#                 [recursion] 'find' list is [[1, 2, 3, 4, 5]]     =>      3
#                 [recursion] 'find' list is [[3, 4, 5]]   =>      4
#                 [recursion] 'find' list is [[4, 5]]      =>      5
#                 [recursion] 'find' list is [[5]]         =>      5
#         result_list is [[None, 1, None]]
# ====================
# target number is **9**, sorted_list is [[1, 2, 3, 4, 5]]
#                 [recursion] 'find' list is [[1, 2, 3, 4, 5]]     =>      3
#                 [recursion] 'find' list is [[3, 4, 5]]   =>      4
#                 [recursion] 'find' list is [[4, 5]]      =>      5
#                 [recursion] 'find' list is [[5]]         =>      5
# None
#                 [recursion] 'find' list is [[1, 2, 3, 4, 5]]     =>      3
#                 [recursion] 'find' list is [[3, 4, 5]]   =>      4
#                 [recursion] 'find' list is [[4, 5]]      =>      5
#                 [recursion] 'find' list is [[5]]         =>      5
#         result_list is [[None, 1, None, None]]
# ====================
# target number is **5**, sorted_list is [[1, 2, 3, 4, 5]]
#                 [recursion] 'find' list is [[1, 2, 3, 4, 5]]     =>      3
#                 [recursion] 'find' list is [[3, 4, 5]]   =>      4
#                 [recursion] 'find' list is [[4, 5]]      =>      5
# ***** FIND!  ***** =>  5
# None
#                 [recursion] 'find' list is [[1, 2, 3, 4, 5]]     =>      3
#                 [recursion] 'find' list is [[3, 4, 5]]   =>      4
#                 [recursion] 'find' list is [[4, 5]]      =>      5
# ***** FIND!  ***** =>  5
#         result_list is [[None, 1, None, None, None]]
# ====================