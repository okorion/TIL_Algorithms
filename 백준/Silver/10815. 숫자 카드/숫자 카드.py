import sys
input = sys.stdin.readline

N = int(input())
A_card = set(map(int, input().split()))
M = int(input())
B_card = list(map(int, input().split()))


# print(result_list)

for _ in range(M):
    if B_card[_] in A_card:
        print(1, end=" ")
    else:
        print(0, end=" ")
