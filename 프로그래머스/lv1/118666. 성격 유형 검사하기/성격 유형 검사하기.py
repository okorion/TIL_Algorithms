from collections import defaultdict

def solution(survey, choices):
    answer = ''
    dict = defaultdict(int)
    
    [dict[x] for x in ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']]
    
    for idx, val in enumerate(survey):
        if choices[idx] >= 4:
            dict[val[1]] += choices[idx] - 4
            
        elif choices[idx] < 4:
            dict[val[0]] += abs(choices[idx] - 4)
            
    # print(dict)
    
    if dict['R'] >= dict['T']:
        answer += 'R'
    elif dict['R'] < dict['T']:
        answer += 'T'
        
    if dict['C'] >= dict['F']:
        answer += 'C'
    elif dict['C'] < dict['F']:
        answer += 'F'
        
    if dict['J'] >= dict['M']:
        answer += 'J'
    elif dict['J'] < dict['M']:
        answer += 'M'
        
    if dict['A'] >= dict['N']:
        answer += 'A'
    elif dict['A'] < dict['N']:
        answer += 'N'
    
    return answer