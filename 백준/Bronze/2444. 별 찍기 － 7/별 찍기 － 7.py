import sys

input = sys.stdin.readline

N = int(input())

for _ in range(N * 2 - 1):
    if _ < N:
        print((N - _ - 1) * " " + (_ * 2 + 1) * "*")

    elif _ >= N:
        print((_ - N + 1) * " " + (((2 * N) - _ - 1) * 2 - 1) * "*")
