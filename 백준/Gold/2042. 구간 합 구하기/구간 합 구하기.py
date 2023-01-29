import sys
from math import log2

input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = [0] * (N + 1)
size = 1 << int(log2(N) + 1)    # `<<` 비트 연산자 => 10<<1 = 20, 10<<2 = 40
tree = [0] * (size * 2)


def seg_update(node, start, end, index, diff):
    if index < start or index > end:
        return
    tree[node] += diff
    if start != end:
        mid = (start + end) // 2
        seg_update(node * 2, start, mid, index, diff)
        seg_update(node * 2 + 1, mid + 1, end, index, diff)


def seg_sum(node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return seg_sum(node * 2, start, mid, left, right) + seg_sum(node * 2 + 1, mid + 1, end, left, right)


for i in range(1, N + 1):
    arr[i] = int(input())
    seg_update(1, 0, N, i, arr[i])

for i in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        diff = c - arr[b]
        arr[b] = c
        seg_update(1, 0, N, b, diff)
    else:
        print(seg_sum(1, 0, N, b, c))

        
# chatGPT 코드, 세그먼트 트리