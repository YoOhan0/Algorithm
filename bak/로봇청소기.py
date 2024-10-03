import sys

input=sys.stdin.readline

N,M=map(int,input().split())
r,c,d=map(int,input().split())

rooms=[]
isCleaned=[[False]*M for _ in range(N)]

dy=(-1,0,1,0) # dy,dx의 인덱스가 i일 때, 0 -> 북쪽, 1 -> 동쪽, 2 -> 남쪽, 3 -> 서쪽
dx=(0,1,0,-1)
rear={0:2,1:3,2:0,3:1} # 후진( 0->2, 1->3, 2->0, 3->1) -> dic 활용
for _ in range(N):
    rooms.append(list(map(int,input().split())))

cnt=0
curY,curX,curDir=r,c,d # 시작 위치

while True:

    if isCleaned[curY][curX]==False: # 과정 1
        isCleaned[curY][curX]=True
        cnt+=1
    
    tmpCnt=0
    for i in range(4): # 과정 2,3 분기 조건
        nextY=curY+dy[i]
        nextX=curX+dx[i]
        
        if rooms[nextY][nextX]==0 and isCleaned[nextY][nextX]==False:
            tmpCnt+=1

    if tmpCnt==0: # 과정 2
        nextDir=rear[curDir]
        nextY=curY+dy[nextDir]
        nextX=curX+dx[nextDir]
        if rooms[nextY][nextX]==0: # 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
            curY=nextY
            curX=nextX
        else: # 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
            break
    else: # 과정 3
        nextDir=curDir=(4+curDir-1)%4 # 반시계[(4+N-1)//4] 방향 90도 회전.
        nextY=curY+dy[nextDir]
        nextX=curX+dx[nextDir]
        if rooms[nextY][nextX]==0 and isCleaned[nextY][nextX]==False: # 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
            curY=nextY
            curX=nextX
        

print(cnt)
