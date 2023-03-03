import sys
from collections import deque

input = sys.stdin.readline

visited = dict()
array = ""


def bfs():
    dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
    queue = deque([array])
    visited[array] = 0

    while queue:
        temp_str = queue.popleft()

        if temp_str == "123456780":
            return visited[temp_str]

        zero_idx = temp_str.find("0")
        zero_col = zero_idx // 3
        zero_row = zero_idx % 3

        for _ in range(4):
            nx = zero_col + dx[_]
            ny = zero_row + dy[_]

            if 0 <= nx < 3 and 0 <= ny < 3:
                idx = nx * 3 + ny
                temp_array = list(temp_str)    # "1234" -> ["1", "2", "3", "4"] -> ["1", "3", "2", "4"] -> "1324" 변환 작업
                temp_array[idx], temp_array[zero_idx] = temp_array[zero_idx], temp_array[idx]
                new_array = "".join(temp_array)

                if not visited.get(new_array):   # dictionary인 visited에서 바뀐 문자열 유무 탐색, 없으면 새로 만드는 작업
                    visited[new_array] = visited[temp_str] + 1
                    queue.append(new_array)

    return -1


for _ in range(3):
    a, b, c = map(str, input().split())
    array += a + b + c

print(bfs())
