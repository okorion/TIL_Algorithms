import sys

input = sys.stdin.readline

G = int(input())
P = int(input())

plane_list = []
result = 0

for _ in range(P):
    plane_list.append(int(input()))

gate_parent = [i for i in range(G+1)]


def find(plane):
    if gate_parent[plane] == plane:
        return gate_parent[plane]
    gate_parent[plane] = find(gate_parent[plane])
    return gate_parent[plane]


for plane in plane_list:
    temp = find(plane)
    if temp == 0:
        break
    gate_parent[temp] = gate_parent[temp-1]    # 공항에 비행기 주차한 경우
    result += 1

print(result)
