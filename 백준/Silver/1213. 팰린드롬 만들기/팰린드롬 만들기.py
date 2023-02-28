import sys
from collections import Counter
input = sys.stdin.readline

temp_str = list(input().strip())
temp_str.sort()
result_list = [[] for _ in range(len(temp_str))]
count_str = Counter(temp_str)

for _ in count_str:
    a = count_str[_]
    # print('a=', a, '_=', _)
    if a % 2:
        result_list[len(temp_str)//2] = _
        count_str[_] -= 1
        a -= 1
        # print(result_list)

    while a != 0:
        for temp in range(len(temp_str)//2):
            if len(result_list[temp]) == 0 and a % 2 == 0 and a != 0:
                result_list[temp] = _
                result_list[-temp-1] = _
                count_str[_] -= 2
                a -= 2
                # print(result_list)

if [] in result_list:
    print("I'm Sorry Hansoo")
    exit(0)
else:
    print(''.join(result_list))
