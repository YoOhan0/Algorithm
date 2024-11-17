import sys
input=sys.stdin.readline
INF=1987654321

N=int(input())

graph=[list(map(int,input().split())) for _ in range(N)]
dist=[[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if graph[i][j]==0:
            dist[i][j]=INF
        else:
            dist[i][j]=graph[i][j]

for node in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j]=min(dist[i][j],dist[i][node]+dist[node][j])


for i in range(N):
    for j in range(N):
        if dist[i][j]==INF: print(0,end=' ')
        else: print(1,end=' ')
    print()