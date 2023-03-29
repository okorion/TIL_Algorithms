import sys
from math import *

input = sys.stdin.readline

N, M = map(int, input().split())


def fill_tree(start, end, idx):
    if start == end:
        tree[idx] = n_list[start]
        return tree[idx]

    mid = (start + end) // 2
    tree[idx] = min(fill_tree(start, mid, idx * 2), fill_tree(mid + 1, end, idx * 2 + 1))

    return tree[idx]


def search_tree(start, end, idx, x, y):
    if x > end or y < start:
        return 1000000001

    if x <= start and y >= end:
        return tree[idx]

    mid = (start + end) // 2
    start = search_tree(start, mid, idx * 2, x, y)
    end = search_tree(mid + 1, end, idx * 2 + 1, x, y)

    return min(start, end)


n_list = []
result_list = []

# 세그먼트 트리 만들기

h = int(ceil(log2(N)))
tree_size = 1 << (h + 1)

tree = [0] * tree_size

for _ in range(N):
    n_list.append(int(input()))

fill_tree(0, N - 1, 1)

for _ in range(M):
    result_list.append(list(map(int, input().split())))

for a, b in result_list:
    print(search_tree(0, N - 1, 1, a - 1, b - 1))

# print(n_list)
# print(result_list)
