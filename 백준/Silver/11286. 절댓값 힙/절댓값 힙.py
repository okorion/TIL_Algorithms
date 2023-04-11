import sys
from heapq import heappop, heappush

input = sys.stdin.readline

N = int(input())
plus_temp_list = []
minus_temp_list = []

for _ in range(N):
    tmp = int(input())
    # print('plus', plus_temp_list)
    # print('minus', minus_temp_list)
    if tmp > 0:
        heappush(plus_temp_list, tmp)
    elif tmp < 0:
        heappush(minus_temp_list, -tmp)
    elif tmp == 0:
        if plus_temp_list:
            if minus_temp_list:
                if plus_temp_list[0] < minus_temp_list[0]:
                    print(heappop(plus_temp_list))

                else:
                    print(-heappop(minus_temp_list))
    
            else:
                print(heappop(plus_temp_list))

        elif minus_temp_list:
            print(-heappop(minus_temp_list))

        else:
            print(0)
