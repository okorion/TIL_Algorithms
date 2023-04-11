import sys
from itertools import combinations

input = sys.stdin.readline

while True:
    n, *lotto_list = list(map(int, input().split()))

    if n == 0:
        break

    # print(n, lotto_list)

    for _ in combinations(lotto_list, 6):
        print(*_)
    print()
