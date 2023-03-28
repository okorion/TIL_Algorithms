import sys

input = sys.stdin.readline

pipe_list = str(input())
pipe_list = pipe_list.replace('()', 'T')
# print(pipe_list)

answer = 0
cut_cnt = 0

for _ in pipe_list:
    if _ == 'T':
        answer += cut_cnt

    elif _ == '(':
        cut_cnt += 1

    elif _ == ')':
        answer += 1
        cut_cnt -= 1

print(answer)
