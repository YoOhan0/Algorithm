import sys
from collections import deque
input=sys.stdin.readline

MAX=1987654321

def solution(row,col,cnt):
    global visitCnt
    place[row][col]=1
    if cnt==3:
        visitCnt+=1    
        returnValue=bfs(visitCnt)
        place[row][col]=0
        return returnValue
    
    minCnt=MAX

    nextRow=row
    nextCol=col
    while nextRow<N and nextCol<M:
        if place[nextRow][nextCol]==0:
            minCnt=min(minCnt,solution(nextRow,nextCol,cnt+1))
        if nextCol==M-1:
            nextRow+=1
            nextCol=0
        else:
            nextCol+=1

    place[row][col]=0
    return minCnt

def bfs(visitValue):
    q=deque(virus)

    cnt=0
    while q:
        curRow,curCol=q.popleft()
        for i in range(4):
            nextRow=curRow+dy[i]
            nextCol=curCol+dx[i]
            if 0<=nextRow<N and 0<=nextCol<M and not place[nextRow][nextCol] and isVisited[nextRow][nextCol]!=visitValue:
                isVisited[nextRow][nextCol]=visitValue
                q.append((nextRow,nextCol))
                cnt+=1

    return cnt
        

N,M=map(int,input().split())

place=[]
virus=[]
dy=[0,0,-1,1]
dx=[-1,1,0,0]
nomalCnt=0
isVisited=[[0]*M for _ in range(N)]
visitCnt=0

for _ in range(N):
    place.append(list(map(int,input().split())))

for i in range(N):
    for j in range(M):
        if place[i][j]==0: nomalCnt+=1
        elif place[i][j]==2: virus.append((i,j)) 

answer=MAX
for i in range(N):
    for j in range(M):
        if place[i][j]==0:
            answer=min(answer,solution(i,j,1))

print(nomalCnt-3-answer)