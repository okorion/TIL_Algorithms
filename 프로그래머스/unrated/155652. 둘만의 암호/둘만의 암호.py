def solution(s, skip, index):
    answer = ''
    
    s_list = list(s)
    print(s_list)
    
    for idx, val in enumerate(s_list):
        cnt = 0
        tmp = ord(val)
        num = 1
        
        while cnt < index:    
            if tmp + num > 122:
                tmp = tmp - 26
            print(tmp, num, chr(tmp+num))
                
            if chr(tmp + num) not in skip:
                num += 1
                cnt += 1
            else:
                num += 1
                
            
        
            print(tmp, num, chr(tmp+num), 'after')

        s_list[idx] = chr(tmp + num - 1)
    
    print(s_list)
    
    for _ in s_list:
        answer += _
    
    return answer