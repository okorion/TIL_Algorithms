import sys

N = int(sys.stdin.readline())

N_2 = [N] + list(str(N))
N_3 = list(map(int, N_2))
temp_len = len(N_3) - 1

hard_cording = [0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 10, 6, 11, 7, 12, 8, 13]

if N < 18:
    print(hard_cording[N])
else:
    temp_list = []

    T = temp_len            # 테스트는 N에서 T * 9 뺀 만큼의 범위 안에서 진행하면 된다.
                            # N => 216, N-T*9 => 189
    for _ in range(N-T*9, N+1):
        temp_list.append(_)

    temp_sum = 0
    result_list = []
    result_temp_num = 1000001

    # print(temp_list)
    for __ in temp_list:    # temp_list => [189, 190, 191, 192, 193, 194, 195, 196, 197, 198, ~ , 215, 216]
        temp_result = list(map(int, list(str(__)))) + [__]
        result_list.append(sum(temp_result))

    cnt = 0

    for ___ in result_list:    # result_list => [207, 200, 202, 204, 206, 208, 210, 212, 214, 216, ~ , 223, 225]
        if N == ___:
            print(temp_list[result_list.index(___)])  # index로 제일 앞에 오는 (N과 같은 값) 찾아서 출력
            break
        cnt += 1

    if cnt == len(result_list):
        print(0)
