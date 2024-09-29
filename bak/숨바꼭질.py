from collections import deque
import sys

input=sys.stdin.readline

MAX=100000

N,K= map(int,input().split())
isVisited=[False for _ in range(100001)]

q=deque([(N,0)])
isVisited[N]=True

while q:

    cur=q.popleft()
    tmpN=cur[0]
    tmpCnt=cur[1]

    if tmpN==K:
        print(tmpCnt)
        break
    
    for next in (tmpN-1, 2*tmpN, tmpN+1):
        if 0<=next<=MAX and not isVisited[next]:
            isVisited[next]=True
            q.append((next,tmpCnt+1))

        


    