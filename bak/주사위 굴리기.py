import sys
input=sys.stdin.readline

# 동쪽 -> 1->3, 3->6, 6->4, 4->1
# 서쪽 -> 1->4, 4->6, 6->3, 3->1
# 북쪽 -> 1->2, 2->6, 6->5, 5->1
# 남쪽 -> 1->5, 5->6, 6->2, 2->1

EAST=1
WEST=2
NORTH=3
SOUTH=4


def solution(curY,curX,commands):
    dy=[0,0,0,-1,1]
    dx=[0,1,-1,0,0]

    for command in commands:
        nextY=curY+dy[command]
        nextX=curX+dx[command]
        if 0<=nextY<N and 0<=nextX<M:
            changeDiceDir(command)
            if Map[nextY][nextX]==0:
                Map[nextY][nextX]=dice[6]
            else:
                dice[6]=Map[nextY][nextX]
                Map[nextY][nextX]=0
            print(dice[1])
            curY=nextY
            curX=nextX

def changeDiceDir(dir):
    steps=[[],[1,4,6,3],[1,3,6,4],[1,5,6,2],[1,2,6,5]] # 동,서,북,남
    
    tmp=dice[1]
    for i in range(len(steps[dir])):
        if i==len(steps[dir])-1: dice[steps[dir][i]]=tmp
        else: dice[steps[dir][i]]=dice[steps[dir][i+1]]

N,M,x,y,K=map(int,input().split())

Map=[]
dice=[0]*7

for _ in range(N):
    Map.append(list(map(int,input().split())))

commands=list(map(int,input().split()))

solution(x,y,commands)