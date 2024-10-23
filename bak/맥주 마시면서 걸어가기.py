import sys
input=sys.stdin.readline
INF=1987654321

T=int(input())
for _ in range(T):
    
    N=int(input())
    start=tuple(map(int,input().split()))
    spots=[]
    spots.append(start) # index 0 -> start
    for _ in range(N):
        spots.append(tuple(map(int,input().split())))
    
    festival=tuple(map(int,input().split()))
    spots.append(festival) # index N+1 -> festival

    graph=[[INF]*(N+2) for _ in range(N+2)] # 플로이드 워셜 사용 할 때는 그래프를 2차원 배열 형식으로 구성하는게 좋은 듯
    for i in range(N+2):
        for j in range(i+1,N+2):
            dist=abs(spots[i][0]-spots[j][0])+abs(spots[i][1]-spots[j][1])
            if dist<=1000:
                graph[i][j]=1
                graph[j][i]=1

    for node in range(N+2):
        for i in range(N+2):
            for j in range(N+2):
                graph[i][j]=min(graph[i][j],graph[i][node]+graph[node][j])

    if graph[0][N+1]!=INF:
        print('happy')
    else:
        print('sad')