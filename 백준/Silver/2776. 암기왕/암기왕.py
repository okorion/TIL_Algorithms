import sys

sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

T = int(input())


def bisect(temp_list, x):
    start = 0
    end = N - 1

    while start <= end:
        mid = (start + end) // 2

        if temp_list[mid] == x:
            return 1
        elif temp_list[mid] < x:
            start = mid + 1
        elif temp_list[mid] > x:
            end = mid - 1

    return 0


for _ in range(T):
    N = int(input())
    A_list = list(map(int, input().split()))
    M = int(input())
    B_list = list(map(int, input().split()))

    A_list.sort()
    
    for _ in B_list:
        print(bisect(A_list, _))

