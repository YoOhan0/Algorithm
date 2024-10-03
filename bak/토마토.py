import sys
from collections import deque

input= sys.stdin.readline

M,N=map(int,input().split())

box=[]
dy=[-1,1,0,0]
dx=[0,0,-1,1]

for _ in range(N):
    box.append(list(map(int,input().split())))
 
def bfs(): # 전역에 적는 것 보다 함수화 시키니까 더 빠른듯?
    q=deque()

    for i in range(N):
        for j in range(M):
            if box[i][j]==1:
                q.append((i,j))

    while q: # 여러 개를 시작점으로 하는 bfs 진행
        cur=q.popleft()

        for i in range(4):
            nextY= cur[0]+dy[i]
            nextX=cur[1]+dx[i]

            if 0<=nextY<N and 0<=nextX<M and box[nextY][nextX]==0:
                box[nextY][nextX]=box[cur[0]][cur[1]]+1
                q.append((nextY,nextX))

    maxNum=0
    for i in range(N): # 만약 토마토 중 안 익은 토마토가 여전히 있다면?
        for j in range(M):
            if box[i][j]==0:
                return -1
                
            else : maxNum=max(maxNum,box[i][j])
    return maxNum-1

print(bfs())            
    


