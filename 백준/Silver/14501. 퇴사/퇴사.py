import sys

input = sys.stdin.readline

N = int(input().strip())

new_list = [0] * (N+1)
T_list = []
P_list = []

for _ in range(N):
    t, p = map(int, input().split())
    T_list.append(t)
    P_list.append(p)

for _ in range(N-1, -1, -1):
    if _ + T_list[_] > N:
        new_list[_] = new_list[_+1]
    else:
        new_list[_] += max(P_list[_] + new_list[_ + T_list[_]], new_list[_+1])

print(new_list[0])