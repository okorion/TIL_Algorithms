import sys

input = sys.stdin.readline

N = int(input())


def starry(len):
    if len == 1:
        return ["*"]

    stars = starry(len//3)
    L = []

    for _ in stars:
        L.append(_*3)
    for _ in stars:
        L.append(_ + " "*(len//3) + _)
    for _ in stars:
        L.append(_*3)

    return L


print("\n".join(starry(N)))
