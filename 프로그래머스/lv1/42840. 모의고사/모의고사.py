def solution(answers):
    answer = []
    
    first_babo = [1,2,3,4,5]
    second_babo = [2,1,2,3,2,4,2,5]
    third_babo = [3,3,1,1,2,2,4,4,5,5]

    first_O = 0
    second_O = 0
    third_O = 0


    for index, first in enumerate(answers):
        if first_babo[index%len(first_babo)] == answers[index]:
            first_O += 1
        if second_babo[index%len(second_babo)] == answers[index]:
            second_O += 1
        if third_babo[index%len(third_babo)] == answers[index]:
            third_O += 1

    max_num = max(first_O, second_O, third_O)
    print(max_num)
    print(first_O, second_O, third_O)
    
    if max_num == 0:
        return []
    if first_O == max_num:
        answer.append(1)
    if second_O == max_num:
        answer.append(2)
    if third_O == max_num:
        answer.append(3)

    return answer