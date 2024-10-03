import sys
from queue import PriorityQueue
input=sys.stdin.readline

INF=1987654321

def solution(start,end):
    
    pq=PriorityQueue()
    weights=[INF]*(N+1)
    
    weights[start]=0
    pq.put((0,start))

    while not pq.empty():
        
        curWeight,cur=pq.get()
        if cur==end: return curWeight
        if curWeight==weights[cur]: # 우선순위 큐에서 특정 노드에 대해, 가장 작은 가중치로 첫 번째로 만나는 것만 로직 수행, 나머지는 무시(굳이 의미 X)
            for next, edgeWeight in graph[cur].items():
                if curWeight+edgeWeight< weights[next]:
                    weights[next]=curWeight+edgeWeight
                    pq.put((weights[next],next))

    return weights[end]

N=int(input())
M=int(input())

graph={i:{} for i in range(N+1)} # graph를 딕셔너리를 사용하여 만들었다(a->b 가 2개이상 있을 경우 효율적)
for _ in range(M):
    start, end, cost= map(int,input().split())
    if end in graph[start]:
        graph[start][end]=min(graph[start][end],cost)
    else : graph[start][end]=cost

start,end=map(int,input().split())
print(solution(start,end))