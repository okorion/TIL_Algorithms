import sys

T = int(sys.stdin.readline())
temp_list = [0] * 2001

for _ in range(T):          # 중복도 가능한 코드
    temp_list[1000 + int(sys.stdin.readline())] += 1

result_list = []
cnt = 0

for __ in range(2001):
    cnt += 1
    if temp_list[__] >= 1:
        for ___ in range(temp_list[__]):
            print(cnt-1001)
