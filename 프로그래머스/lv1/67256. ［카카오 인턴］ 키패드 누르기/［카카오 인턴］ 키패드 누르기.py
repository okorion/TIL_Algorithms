def solution(numbers, hand):
    result_list = []
    new_list = []
    hands = ""
    
    if hand == "right":
        hands = "R"
    elif hand == "left":
        hands = "L"
        
            
    pre_Lnum = 10
    pre_Rnum = 12
    
    for num in numbers:
        if num == 1 or num == 4 or num == 7:
            result_list.append("L")
            pre_Lnum = num
        elif num == 3 or num == 6 or num == 9:
            result_list.append("R")
            pre_Rnum = num
        elif num == 2 or num == 5 or num == 8:
            if abs(pre_Lnum-num)//3 + abs(pre_Lnum-num)%3 == abs(pre_Rnum-num)//3 + abs(pre_Rnum-num)%3:
                result_list.append(hands)
                if hand == "right":
                    pre_Rnum = num
                elif hand == "left":
                    pre_Lnum = num
            elif abs(pre_Lnum-num)//3 + abs(pre_Lnum-num)%3 > abs(pre_Rnum-num)//3 + abs(pre_Rnum-num)%3:
                result_list.append("R")
                pre_Rnum = num
            elif abs(pre_Lnum-num)//3 + abs(pre_Lnum-num)%3 < abs(pre_Rnum-num)//3 + abs(pre_Rnum-num)%3:
                result_list.append("L")
                pre_Lnum = num
                
        elif num == 0:
            num += 11
            if abs(pre_Lnum-num)//3 + abs(pre_Lnum-num)%3 == abs(pre_Rnum-num)//3 + abs(pre_Rnum-num)%3:
                result_list.append(hands)
                if hand == "right":
                    pre_Rnum = num
                elif hand == "left":
                    pre_Lnum = num
            elif abs(pre_Lnum-num)//3 + abs(pre_Lnum-num)%3 > abs(pre_Rnum-num)//3 + abs(pre_Rnum-num)%3:
                result_list.append("R")
                pre_Rnum = num
            else:
                result_list.append("L")
                pre_Lnum = num
                
    return "".join(result_list)