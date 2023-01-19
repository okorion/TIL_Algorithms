import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())

gem_list = []
bag_list = []

for _ in range(N):    # 보석 무게 M_i, 가격 V_i, 가방 하나에 보석 한 개
    M_i, V_i = map(int, input().split())
    gem_list.append([M_i, V_i])
for _ in range(K):    # K개의 가방에 담을 수 있는 최대 무게 C_i
    C_i = int(input())
    bag_list.append(C_i)

gem_list.sort()
bag_list.sort()

temp = []
result = 0

for i in bag_list:
    while gem_list and gem_list[0][0] <= i:
        heapq.heappush(temp, -gem_list[0][1])
        heapq.heappop(gem_list)

    if temp:
        # print(i, temp)
        result += heapq.heappop(temp)

print(-result)
