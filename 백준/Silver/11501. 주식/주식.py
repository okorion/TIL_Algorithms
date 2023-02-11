import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    price = list(map(int, input().split()))
    result = 0
    max_val = price[-1]

    for i in range(N-2, -1, -1):
        if price[i] > max_val:
            max_val = price[i]
        else:
            result += max_val - price[i]

    print(result)
