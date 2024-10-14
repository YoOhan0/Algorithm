import sys
input=sys.stdin.readline
MAX=1987654321

def solution(ladders,idx,cnt):
    global coord,coordNum,answer

    if answer<=cnt: return 
    if cnt>3:return

    ladders[coord[idx][0]][coord[idx][1]]=True

    falseNum=executeLadders(ladders)
    if not falseNum:
        answer=min(answer,cnt)
        ladders[coord[idx][0]][coord[idx][1]]=False
        return

    if falseNum>2*(3-cnt): 
        ladders[coord[idx][0]][coord[idx][1]]=False
        return 
    
    for nextIdx in range(idx+1,coordNum):
        nextR=coord[nextIdx][0]
        nextC=coord[nextIdx][1]
        if not ladders[nextR][nextC-1] and not ladders[nextR][nextC+1]:
            solution(ladders,nextIdx,cnt+1)
    
    ladders[coord[idx][0]][coord[idx][1]]=False
    return

def executeLadders(ladders):
    falseNum=0
    for i in range(1,N+1):
        curCol=i
        for j in range(1,H+1):
            if ladders[j][curCol-1]: curCol-=1
            elif ladders[j][curCol]: curCol+=1
        if i!=curCol: falseNum+=1
    return falseNum

N,M,H=map(int,input().split())
ladders=[[False]* (N+1) for _ in range(H+1)] # 행 : 1 ~ H, 열 1 ~ N
for _ in range(M):
    a,b=map(int,input().split())
    ladders[a][b]=True

coord=[]
for i in range(1,H+1):
    for j in range(1,N):
        if not ladders[i][j]: coord.append((i,j))

coordNum=len(coord)
answer=MAX

if not executeLadders(ladders): print(0)
else:
    for idx in range(coordNum):
        solution(ladders,idx,1)

    if answer==MAX: print(-1)
    else: print(answer)