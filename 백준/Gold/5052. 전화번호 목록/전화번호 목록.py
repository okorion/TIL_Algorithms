import sys

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    result = False
    T = int(input())
    call_list = [input().strip() for _ in range(T)]
    call_list.sort()
    result = True

    for c in range(T - 1):
        if call_list[c] == call_list[c+1][:len(call_list[c])]:
            result = False
            break

    if result:
        print('YES')
    else:
        print('NO')
