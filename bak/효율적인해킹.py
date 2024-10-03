import sys
from collections import deque

def bfs(start):
    global visitedNum
    q=deque([start])
    isVisited[start]=visitedNum

    cnt=0
    while q:
        cur=q.pop()
        cnt+=1
        for next in trusts[cur]:
            if isVisited[next]!=visitedNum:
                isVisited[next]=visitedNum
                q.append(next)
    visitedNum+=1
    return cnt

input= sys.stdin.readline

N,M=map(int,input().split())
trusts=[[] for _ in range(N+1)]
isVisited=[0 for _ in range(N+1)]
visitedNum=1

for _ in range(M):
    A,B=map(int,input().split())
    trusts[B].append(A)

bucket=[]
for i in range(1,N+1):
    bucket.append((i,bfs(i)))

bucket.sort(key=lambda x:(-x[1],x[0]))

for item in bucket: 
    if item[1]==bucket[0][1]: print(item[0],end=" ")