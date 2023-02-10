import sys
input = sys.stdin.readline

N, M = map(int, input().split())
list_6 = []
list_1 = []

# print(N, M)

for _ in range(M):
    ex_6, ex_1 = map(int, input().split())
    list_6.append(ex_6)
    list_1.append(ex_1)

list_6.sort()
list_1.sort()

# print(list_6, list_1)

if N // 6:
    if min(list_6) >= 6 * min(list_1):
        print(N * min(list_1))
        # print(min(list_6), min(list_1))
    else:
        if min(list_6) <= (N % 6) * min(list_1):
            print(((N // 6) + 1) * min(list_6))
        else:
            print(((N // 6) * min(list_6)) + ((N % 6) * min(list_1)))
        # print(min(list_6), min(list_1), (N % 6), 'else')
else:
    if min(list_6) <= (N % 6) * min(list_1):
        print(((N // 6) + 1) * min(list_6))
    else:
        print((N % 6) * min(list_1))
