import sys
from queue import PriorityQueue
input=sys.stdin.readline
INF=1987654321

def shortestPath(graph,start):
    dist=[INF]*(N+1)
    pq=PriorityQueue()
    
    dist[start]=0
    pq.put((0,start))

    while not pq.empty():
        curDist,curIdx=pq.get()
        
        if curDist>dist[curIdx]:continue

        for nextIdx,edgeDist in graph[curIdx]:
            if curDist+edgeDist< dist[nextIdx]:
                dist[nextIdx]=curDist+edgeDist
                pq.put((dist[nextIdx],nextIdx))
    return dist

N,M,X=map(int,input().split())

graph=[[] for _ in range(N+1)]
rev_graph=[[] for _ in range(N+1)]
for _ in range(M):
    a,b,c= map(int,input().split())
    graph[a].append((b,c))
    rev_graph[b].append((a,c))

to_X=shortestPath(rev_graph,X)
from_X=shortestPath(graph,X)

answer=0
for i in range(1,N+1):
    answer=max(answer,to_X[i]+from_X[i])

print(answer)