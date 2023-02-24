import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    queue = deque(map(int, input().split())) #[1,1,9,1,1,1]
    temp_list = deque(range(N))  #[1,2,3,4,5,6]
    cnt = 0
    target = temp_list[M]

    # print(queue)

    while True:
        # print(queue)
        if queue[0] != max(queue):
            queue.rotate(-1)
            temp_list.rotate(-1)
            # print('cnt', queue)
        else:
            cnt += 1
            if target == temp_list[0]:
                print(cnt)
                # print(queue, 1111)
                break

            queue.popleft()
            temp_list.popleft()
