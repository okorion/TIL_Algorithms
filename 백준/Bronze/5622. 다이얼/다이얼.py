import sys

input = sys.stdin.readline

temp_list = list(str(input()))

result_list = [[0], [0], [0], ["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"],
               ["J", "K", "L"], ["M", "N", "O"], ["P", "Q", "R", "S"], ["T", "U", "V"],
               ["W", "X", "Y", "Z"]]

idx = -1
answer = []

for _ in result_list:
    idx += 1
    for a in temp_list:
        if a in _:
            answer.append(idx)

print(sum(answer))
