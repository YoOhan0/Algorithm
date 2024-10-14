import sys
input=sys.stdin.readline

RIGHT=0
UP=1
LEFT=2
DOWN=3

def makeDragon(board,start,startDir,gen):
    
    steps=[startDir]
    curGen=1
    while curGen<=gen:
        for i in range(len(steps)-1,-1,-1):
            if steps[i]==UP: steps.append(LEFT)
            elif steps[i]==LEFT: steps.append(DOWN)
            elif steps[i]==RIGHT: steps.append(UP)
            elif steps[i]==DOWN: steps.append(RIGHT)
        curGen+=1
    
    curY=start[0]
    curX=start[1]
    for i in range(len(steps)):
        board[curY][curX]=True
        curY+=dy[steps[i]]
        curX+=dx[steps[i]]
    board[curY][curX]=True

    return
    
board=[[False]*101 for _ in range(101)]
dy=[0,-1,0,1]
dx=[1,0,-1,0]
N=int(input())

for _ in range(N):
    x,y,d,g=map(int,input().split())
    makeDragon(board,(y,x),d,g)

answer=0
for i in range(100):
    
    for j in range(100):
        tmpNum=0
        tmpNum+=board[i][j]
        tmpNum+=board[i][j+1]
        tmpNum+=board[i+1][j]
        tmpNum+=board[i+1][j+1]
        if tmpNum==4: answer+=1

print(answer)