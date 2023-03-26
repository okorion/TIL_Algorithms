import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline

N, M = map(int, input().split())


def fill_tree(start, end, idx, tree):
    if start == end:
        tree[idx] = (temp_list[start], temp_list[end])
        return tree[idx]

    mid = (start + end) // 2
    start = fill_tree(start, mid, 2 * idx + 1, tree)
    end = fill_tree(mid + 1, end, 2 * idx + 2, tree)

    tree[idx] = (min(start[0], end[0]), max(start[1], end[1]))

    return tree[idx]


def search_tree(start, end, idx, tree, x, y):
    if x > end or y < start:
        return (1000000001, 0)

    if x <= start and y >= end:
        return tree[idx]

    mid = (start + end) // 2

    start = search_tree(start, mid, 2 * idx + 1, tree, x, y)
    end = search_tree(mid + 1, end, 2 * idx + 2, tree, x, y)

    return (min(start[0], end[0]), max(start[1], end[1]))


temp_list = []

for _ in range(N):
    temp_list.append(int(input()))

size_node = 1

while size_node < N:
    size_node <<= 1
size_node <<= 1

seg_tree = [0] * size_node

fill_tree(0, N - 1, 0, seg_tree)

for _ in range(M):
    a, b = map(int, input().split())
    print(*search_tree(0, N - 1, 0, seg_tree, a - 1, b - 1))
