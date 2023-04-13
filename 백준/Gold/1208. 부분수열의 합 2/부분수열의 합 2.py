import sys
from itertools import combinations
from collections import defaultdict

input = sys.stdin.readline

N, S = map(int, input().split())
tmp_arr = list(map(int, input().split()))
answer = 0


def fill_dict(arr: list, tmp: defaultdict):
    for _ in range(1, len(arr) + 1):
        for c in combinations(arr, _):
            tmp[sum(c)] += 1


left_dict = defaultdict(int)
right_dict = defaultdict(int)

fill_dict(tmp_arr[:N//2], left_dict)
fill_dict(tmp_arr[N//2:], right_dict)

answer += left_dict[S] + right_dict[S]

for s1 in left_dict:
    if S - s1 in right_dict:
        answer += left_dict[s1] * right_dict[S - s1]

print(answer)
