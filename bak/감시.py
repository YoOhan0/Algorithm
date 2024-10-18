import sys
from collections import deque
INF=1987654321
input=sys.stdin.readline

def solution(curIdx,moveTypes):
    global cctvs,cctvTypes,cctvLen,answer
    if curIdx==cctvLen:
        tmp=bfs(moveTypes)
        if answer>tmp: answer=tmp
        return
    for i in range(len(cctvTypes[cctvs[curIdx][2]])):
        solution(curIdx+1,moveTypes+[i])
    return

def bfs(moveTypes):
    global cctvs,cctvTypes,cctvLen,room,N,M
    visited=[[False]*M for _ in range(N)]

    q=deque([])
    for i in range(cctvLen):
        for dir in cctvTypes[cctvs[i][2]][moveTypes[i]]:
            q.append((cctvs[i][0],cctvs[i][1],dir))

    while q:
        curY,curX,curDir = q.popleft()
        
        nY=curY+curDir[0]
        nX=curX+curDir[1]

        if 0<=nY<N and 0<=nX<M and room[nY][nX]!=6:
            visited[nY][nX]=True
            q.append((nY,nX,curDir))

    answer=0
    for i in range(N):
        for j in range(M):
            if room[i][j]==0 and not visited[i][j]:
                answer+=1

    return answer            

N,M=map(int,input().split())
room=[list(map(int,input().split())) for _ in range(N)]
#ccvt[가능한 cctv 종류][가능한 move유형]
cctvTypes=[[],
           [[(0,-1)],[(0,1)],[(1,0)],[(-1,0)]],
           [[(-1,0),(1,0)],[(0,-1),(0,1)]],
           [[(-1,0),(0,1)],[(-1,0),(0,-1)],[(1,0),(0,1)],[(1,0),(0,-1)]],
           [[(-1,0),(1,0),(0,-1)],[(1,0),(0,-1),(0,1)],[(-1,0),(0,-1),(0,1)],[(-1,0),(1,0),(0,1)]],
           [[(-1,0),(1,0),(0,-1),(0,1)]]
           ]
               
cctvs=[]
cctvLen=0
answer=INF
for i in range(N):
    for j in range(M):
        if 1<=room[i][j]<=5: 
            cctvs.append((i,j,room[i][j]))
            cctvLen+=1

solution(0,[])
print(answer)