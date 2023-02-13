def solution(today, terms, privacies):
    today_y = int(today[2:4])
    today_m = int(today[5:7])
    today_d = int(today[8:10])
    today_day = today_y * 12 * 28 + today_m * 28 + today_d
    
    terms_list = []
    answer = []
    
    for t in range(len(terms)):
        a, b = terms[t].split()
        terms_list.append([a, b])
        
    for _ in range(len(privacies)):
        p_y = int(privacies[_][2:4])
        p_m = int(privacies[_][5:7])
        p_d = int(privacies[_][8:10])
        p_day = p_y * 12 * 28 + p_m * 28 + p_d
        
        temp_list = []
        
        for term in range(len(terms_list)):
            a, b = terms[term].split()
            if privacies[_][-1] == a:
                p_day += int(b) * 28
                
                if today_day >= p_day:
                    answer.append(_ + 1)
        
    return answer