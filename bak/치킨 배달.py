import sys
input=sys.stdin.readline
MAX=1987654321
def solution(idx,cnt):

    global chickens,picks,answer
    picks.append(chickens[idx])
    if cnt==M:
        answer=min(answer,calDistance())
        picks.pop()
        return

    for nextIdx in range(idx+1,chickenLen):
        solution(nextIdx,cnt+1)
    
    picks.pop()
    return

def calDistance():
    global picks,homes
    total=0
    for i in homes:
        tmpMin=MAX
        for j in picks:
            cur=abs(i[0]-j[0])+abs(i[1]-j[1])
            if tmpMin>cur: tmpMin=cur
        total+=tmpMin
    
    return total

N,M=map(int,input().split())

city=[]
for _ in range(N):
    city.append(list(map(int,input().split())))

homes=[]
chickens=[]
picks=[]
for i in range(N):
    for j in range(N):
        if city[i][j]==1: homes.append((i,j))
        elif city[i][j]==2: chickens.append((i,j))

chickenLen=len(chickens)
answer=MAX

for i in range(chickenLen):
    solution(i,1)

print(answer)