import sys
import heapq
input=sys.stdin.readline
def solution(cards):
    pq=[]
    heapq.heapify(pq)

    for card in cards:
        heapq.heappush(pq,card)
    answer=0
    while len(pq)>=2:
        item1=heapq.heappop(pq)
        item2=heapq.heappop(pq)
        answer+=item1+item2
        heapq.heappush(pq,item1+item2)
    return answer

N=int(input())
cards=[int(input()) for _ in range(N)]
print(solution(cards))