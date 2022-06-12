import sys

N = int(sys.stdin.readline())

for _ in range(N):
    a = list(sys.stdin.readline().rstrip())
    temp_sum = 0
    cnt = 0

    for __ in a:
        if __ == 'X':
            cnt = 0
        elif __ == 'O':
            cnt += 1
            temp_sum += cnt

    print(temp_sum)
