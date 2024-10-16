import sys
input=sys.stdin.readline

def solution(space,circle):
    global R,C
    dy=[0,0,-1,1]
    dx=[-1,1,0,0]
    upBound=circle[0][0]
    downBound=circle[1][0]
    newSpace=[[0]*C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if space[i][j]>0:
                spread=space[i][j]//5
                for k in range(4):
                    nY=i+dy[k]
                    nX=j+dx[k]
                    if 0<=nY<R and 0<=nX<C and space[nY][nX]!=-1:
                        newSpace[nY][nX]+=spread
                        space[i][j]-=spread
                newSpace[i][j]+=space[i][j]

    tmp=newSpace[0][0]
    for i in range(1,C):
        newSpace[0][i-1]=newSpace[0][i]
    for i in range(1,upBound+1):
        newSpace[i-1][C-1]=newSpace[i][C-1]
    for i in range(C-2,-1,-1):
        newSpace[upBound][i+1]=newSpace[upBound][i]
    for i in range(upBound-1,0,-1):
        newSpace[i+1][0]=newSpace[i][0]
    newSpace[1][0]=tmp

    tmp=newSpace[downBound][0]
    for i in range(downBound+1,R):
        newSpace[i-1][0]=newSpace[i][0]
    for i in range(1,C):
        newSpace[R-1][i-1]=newSpace[R-1][i]
    for i in range(R-2,downBound-1,-1):
        newSpace[i+1][C-1]=newSpace[i][C-1]
    for i in range(C-2,-1,-1):
        newSpace[downBound][i+1]=newSpace[downBound][i]
    newSpace[downBound][1]=tmp
    
    newSpace[circle[0][0]][circle[0][1]]=-1
    newSpace[circle[1][0]][circle[1][1]]=-1
    
    return newSpace

R,C,T= map(int,input().split())
space=[]
for _ in range(R):
    space.append(list(map(int,input().split())))

circle=[]
for i in range(R):
    for j in range(C):
        if space[i][j]==-1:
            circle.append((i,j))

for i in range(T):
    space=solution(space,circle)

answer=0
for i in range(R):
    for j in range(C):
        if space[i][j]!=-1: answer+=space[i][j]

print(answer)