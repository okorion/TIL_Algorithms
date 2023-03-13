from heapq import heappush, heappop, heapify

def solution(scoville, K):
    answer = 0
    heapify(scoville)
    
    if scoville[0] >= K:
        return answer
    
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        
        a = heappop(scoville)
        b = heappop(scoville)
        heappush(scoville, a + 2 * b)
        
        answer += 1
        
    return answer