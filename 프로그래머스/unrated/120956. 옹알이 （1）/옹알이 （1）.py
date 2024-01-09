def solution(babbling):
    answer = 0
    temp_set = {"aya", "ye", "woo", "ma"}  # set으로 변경
    tmp = []
    
    for b in babbling:
        for t in temp_set:
            if t in b:
                b = b.replace(t, " ")  # replace 메서드가 반환값을 가지므로 b에 할당
                
                if (b == " " or b == "  " or b == "   " or b == "    "):
                    tmp.append(b)
    
    return len(tmp)
