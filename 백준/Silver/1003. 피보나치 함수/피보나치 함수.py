import sys

T = int(sys.stdin.readline())


def fib(n):
    _curr, _next = 0, 1
    for _ in range(n):
        _curr, _next = _next, _curr + _next
    return _curr, _next


for _ in range(T):
    temp_num = int(sys.stdin.readline())

    if temp_num == 0:
        print("1 0")
    elif temp_num == 1:
        print("0 1")
    else:
        print(f"{fib(temp_num-1)[0]} {fib(temp_num-1)[1]}")
