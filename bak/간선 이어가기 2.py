import sys
import heapq
input=sys.stdin.readline
INF=1987654321

def shortestPath(graph,start,end):
    global N,M

    dist=[INF]*(N+1)
    pq=[]

    dist[start]=0
    heapq.heappush(pq,(0,start))

    while pq:
        curDist,cur=heapq.heappop(pq)
        if curDist>dist[cur]: continue

        for next,edgeW in graph[cur]:

            if curDist+edgeW<dist[next]:
                dist[next]=curDist+edgeW
                heapq.heappush(pq,(dist[next],next))

    return dist[end]

N,M=map(int,input().split())

graph=[[] for _ in range(N+1)]

for _ in range(M):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

s,t=map(int,input().split())

print(shortestPath(graph,s,t))