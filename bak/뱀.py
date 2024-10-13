import sys
from collections import deque
input=sys.stdin.readline

INF=1987654321

def solution(commands):
    snakeCheck=[[False]*N for _ in range(N)]
    q=deque([(0,0)])

    dy=[0,1,0,-1] # 오른쪽, 아래, 왼쪽, 위쪽
    dx=[1,0,-1,0] # 왼쪽(L) 나오면 -> (x-1+4)%4, 오른쪽(D) 나오면, (x+1)%4
    prev=0
    curDir=0 # 처음엔 오른쪽
    curY=0;curX=0
    totalTime=0
    for t,command in commands:
        curTime=t-prev

        while curTime>0:
            # print(f"row,col : {curY},{curX}")
            nextY=curY+dy[curDir]
            nextX=curX+dx[curDir]
           
            if 0<=nextY<N and 0<=nextX<N:
                if snakeCheck[nextY][nextX]:
                    return totalTime+1
                
                snakeCheck[nextY][nextX]=True
                q.append((nextY,nextX))
                if board[nextY][nextX]==0:
                    tmpY,tmpX=q.popleft()
                    snakeCheck[tmpY][tmpX]=False
                elif board[nextY][nextX]==2:
                    board[nextY][nextX]=0                    
            else:
                return totalTime+1
                 
            curY=nextY
            curX=nextX
            totalTime+=1
            curTime-=1
        
        prev=t
        if command=='L':curDir=(curDir-1+4)%4
        else: curDir=(curDir+1)%4   
    
    return -1

N=int(input())
K=int(input())

board=[[0]*N for _ in range(N)]

for _ in range(K):
    a,b=map(int,input().split())
    board[a-1][b-1]=2

L=int(input())

commands=[]
for _ in range(L):
    a,b=input().split()
    commands.append((int(a),b))
commands.append((INF,'D'))

print(solution(commands))