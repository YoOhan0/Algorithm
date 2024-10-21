import sys
import heapq
input=sys.stdin.readline
INF=1987654321

def solution(start):
    global N
    dist=[INF]*(N+1)
    visited=[False]*(N+1)
    dist[start]=0

    pq=[]
    heapq.heappush(pq,(0,start))

    answer=0
    while pq:
        curDist,cur=heapq.heappop(pq)
        if visited[cur]: continue
        else:
            visited[cur]=True
            answer+=curDist

        for next,edgeW in graph[cur]:
            if not visited[next] and dist[next]>edgeW:
                dist[next]=edgeW
                heapq.heappush(pq,(edgeW,next))
    
    for item in dist[1:]:
        if item==INF: return -1
    
    return answer

N=int(input())
M=int(input())

graph=[[] for _ in range(N+1)]

for _ in range(M):
    a,b= map(int,input().split())
    graph[a].append((b,0))
    graph[b].append((a,0))

K=int(input())

for _ in range(K):
    a,b,c=map(int,input().split())

    graph[a].append((b,c))
    graph[b].append((a,c))

print(solution(1))