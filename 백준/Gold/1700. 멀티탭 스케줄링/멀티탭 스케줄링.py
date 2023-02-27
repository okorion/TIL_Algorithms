import sys
input = sys.stdin.readline

N, K = map(int, input().split())
use = list(map(int, input().split()))
plugs = []
result = 0

for _ in range(K):
    if use[_] in plugs:
        continue

    if len(plugs) < N:
        plugs.append(use[_])
        continue

    far_plug = 0  # 플러그 최대 거리 체크
    temp = 0  # 가장 멀리 있는 플러그 찾기

    for plug in plugs:
        if plug not in use[_:]:
            temp = plug
            break
        elif use[_:].index(plug) > far_plug:
            far_plug = use[_:].index(plug)
            temp = plug

    plugs[plugs.index(temp)] = use[_]
    result += 1

print(result)
