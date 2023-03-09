import sys
from bisect import bisect_left

input = sys.stdin.readline

N = int(input())

temp_list = list(map(int, input().split()))

# print(temp_list)
stack = []
result_list = []

for _ in temp_list:
    if not stack or stack[-1] < _:
        stack.append(_)
        result_list.append([bisect_left(stack, _), _])
    else:
        stack[bisect_left(stack, _)] = _    # [20, 10] 에서 초반이 감소하며 시작할 때 보정해주는 코드. 안 넣으면 20보다 작은 수 bisect_left에서 카운트 X
                                            # 쉽게 말해서 초반에 연속으로 감소하면 감소하는 값 제일 마지막을 처음 시작으로 만들어주는 코드.
        result_list.append([bisect_left(stack, _), _])


# print(result_list)

last_idx = len(stack) - 1
result = []

for _ in range(-1, -N-1, -1):
    if result_list[_][0] == last_idx:
        result.append(result_list[_][1])
        last_idx -= 1

print(len(result))
print(*result[::-1])
