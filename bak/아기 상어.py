import sys
from collections import deque
input=sys.stdin.readline

def bfs(space,shark,sharkPower):
    
    visited=[[False]*N for _ in range(N)]
    dy=[-1,0,0,1]
    dx=[0,-1,1,0]
    q=deque([(shark[0],shark[1],0)])

    answer=[]
    while q:
        cur=q.popleft()
        for i in range(4):
            nY=cur[0]+dy[i]
            nX=cur[1]+dx[i]
            if 0<=nY<N and 0<=nX<N and not visited[nY][nX] and space[nY][nX]<=sharkPower:
                if space[nY][nX]!=0 and space[nY][nX]!=sharkPower:
                    answer.append((nY,nX,cur[2]+1))
                visited[nY][nX]=True
                q.append((nY,nX,cur[2]+1))
    
    answer.sort(key=lambda x:(x[2],x[0],x[1]))
    if not len(answer): return None
    else: return answer[0]

N=int(input())
space=[list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if space[i][j]==9:
            space[i][j]=0
            shark=(i,j)

sharkFeed=0
sharkPower=2
answer=0

while True:
    tmp=bfs(space,shark,sharkPower)
    if not tmp: break
    
    answer+=tmp[2]
    space[tmp[0]][tmp[1]]=0
    if sharkFeed+1==sharkPower:
        sharkPower+=1
        sharkFeed=0
    else: sharkFeed+=1
    shark=(tmp[0],tmp[1])

print(answer)