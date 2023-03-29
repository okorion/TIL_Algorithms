from collections import deque

def solution(cards1, cards2, goal):
    q1 = deque()
    q2 = deque()
    
    for _ in cards1:
        q1.append(_)
    for _ in cards2:
        q2.append(_)
        
    for _ in goal:
        if q1 and _ == q1[0]:
            q1.popleft()
        elif q2 and _ == q2[0]:
            q2.popleft()
        else:
            return "No"
    
    return "Yes"