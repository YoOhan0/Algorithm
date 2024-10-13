import sys
input=sys.stdin.readline

LEFT=0
UP=1
RIGHT=2
DOWN=3

MAX=1987654321
def solution(R,B,cnt):
    
    if cnt>=10: return MAX

    minNum=MAX
    for i in range(4):
        
        nRy,nRx,nBy,nBx,result=tiltBoard(R,B,i)
        
        if result==1:
            return cnt+1
        elif R[0]==nRy and R[1]==nRx and B[0]==nBy and B[1]==nBx: continue
        elif result==0:
            minNum=min(minNum,solution((nRy,nRx),(nBy,nBx),cnt+1))

    return minNum
    

def tiltBoard(R,B,dir):
    rY=R[0]
    rX=R[1]
    bY=B[0]
    bX=B[1]
    
    while board[rY+dy[dir]][rX+dx[dir]]==0:
        if dir==LEFT: rX+=-1
        if dir==UP: rY+=-1
        if dir==RIGHT: rX+=1
        if dir==DOWN: rY+=1
    while board[bY+dy[dir]][bX+dx[dir]]==0:
        if dir==LEFT: bX+=-1
        if dir==UP: bY+=-1
        if dir==RIGHT: bX+=1
        if dir==DOWN: bY+=1
    
    if min(R[0],rY)<=S[0]<=max(R[0],rY) and min(R[1],rX) <=S[1]<=max(R[1],rX):
        rFlag=True
    else: rFlag=False
    if min(B[0],bY)<=S[0]<=max(B[0],bY) and min(B[1],bX) <=S[1]<=max(B[1],bX):
        bFlag=True
    else: bFlag=False
    
    if rY==bY and rX==bX:

        if dir==LEFT:
            if R[1]<B[1]:bX+=1
            else: rX+=1
        if dir==UP:
            if R[0]<B[0]:bY+=1
            else: rY+=1
        if dir==RIGHT:
            if R[1]<B[1]:rX+=-1
            else: bX+=-1
        if dir==DOWN:
            if R[0]<B[0]:rY+=-1
            else: bY+=-1

    if bFlag: return (rY,rX,bY,bX,-1)
    elif rFlag: return (rY,rX,bY,bX,1)
    else: return (rY,rX,bY,bX,0)


N,M=map(int,input().split())

board=[[0]*M for _ in range(N)]
dy=[0,-1,0,1]
dx=[-1,0,1,0]

for i in range(N):
    tmp=input()
    for j,item in enumerate(tmp):
        if tmp[j]=='R':
            R=(i,j)
        elif tmp[j]=='B':
            B=(i,j)
        elif tmp[j]=='O':
            S=(i,j)
        elif tmp[j]=='#':
            board[i][j]=1

answer=solution(R,B,0)
if answer==MAX: print(-1)
else: print(answer)