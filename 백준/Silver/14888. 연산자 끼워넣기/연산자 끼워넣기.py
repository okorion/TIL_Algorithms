import sys

input = sys.stdin.readline

N = int(input())
temp_list = list(map(int, input().split()))
result_list = []
p, m, t, d = map(int, input().split())


def four_calculate(n, total, plus, minus, multiply, divided):
    if n == N:
        result_list.append(total)
        return

    else:
        if plus != 0:
            four_calculate(n+1, total + temp_list[n], plus-1, minus, multiply, divided)

        if minus != 0:
            four_calculate(n+1, total - temp_list[n], plus, minus-1, multiply, divided)

        if multiply != 0:
            four_calculate(n+1, total * temp_list[n], plus, minus, multiply-1, divided)

        if divided != 0:
            four_calculate(n+1, int(total / temp_list[n]), plus, minus, multiply, divided-1)


four_calculate(1, temp_list[0], p, m, t, d)

print(max(result_list))
print(min(result_list))
