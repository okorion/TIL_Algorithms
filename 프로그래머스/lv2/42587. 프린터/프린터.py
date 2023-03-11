from collections import deque

def solution(priorities, location):
    t = deque(priorities)
    temp_list = deque(range(len(priorities)))
    cnt = 0
    print(t)
    while True:
        max_value = t.index(max(t))
        t.rotate(-max_value)
        temp_list.rotate(-max_value)

        t.popleft()
        cnt += 1

        if temp_list.popleft() == location:
            return cnt
    