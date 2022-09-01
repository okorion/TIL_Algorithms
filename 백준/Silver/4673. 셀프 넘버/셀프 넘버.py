import sys

input = sys.stdin.readline

temp_list = []

for _ in range(1, 10001):
    if 1 <= _ < 10:
        temp_list.append(_+_)
    elif 10 <= _ < 100:
        temp_list.append(_+_//10+(_%10))
    elif 100 <= _ < 1000:
        temp_list.append(_+_//100+(_%100)//10+(_%10))
    elif 1000 <= _ < 10000:
        temp_list.append(_+_//1000+(_%1000)//100+(_%100)//10+(_%10))

temp_list = set(temp_list)
result_list = set(range(1, 10001))

result_list = result_list - temp_list

for rl in sorted(result_list):
    print(rl)
