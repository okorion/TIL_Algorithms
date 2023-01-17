import sys

input = sys.stdin.readline

N = int(input())

words = []

for _ in range(N):
    words.append(input().strip())

temp_dict = {}

for word in words:
    square_root = len(word) - 1

    for c in word:
        if c in temp_dict:
            temp_dict[c] += pow(10, square_root)
        else:
            temp_dict[c] = pow(10, square_root)
        square_root -= 1

new_dict = sorted(temp_dict.values(), reverse=True)

result = 0
m = 9

for _ in new_dict:
    result += _ * m
    m -= 1

print(result)
