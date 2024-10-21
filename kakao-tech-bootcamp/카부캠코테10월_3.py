import sys
from collections import deque

input=sys.stdin.readline
GROUND=2
SKY=1
BLOCK=0

def solution(vilige,K,T):
	global N,M
	dy=[0,0,-1,1]
	dx=[-1,1,0,0]
	
	visited=[[[False]*(K+1) for _ in range(M)] for _ in range(N)]
	q=deque([(0,0,K,0)])
	visited[0][0][K]=True

	while q:
		curY,curX,curHP,curTime=q.popleft()

		if curY==N-1 and curX==M-1: # 최단 거리 도착하면 종료
			if curTime<=T: return True
			else: return False
        
		if vilige[curY][curX]==GROUND and curHP<K and not visited[curY][curX][curHP+1]: # 쉴 수 있다면, 쉬는 것도 고려
			visited[curY][curX][curHP+1]=True
			q.append((curY,curX,curHP+1,curTime+1))
		
		for dir in range(4):
			nY=curY+dy[dir]
			nX=curX+dx[dir]
		
			if 0<=nY<N and 0<=nX<M and vilige[nY][nX]!=BLOCK: # 현재 좌표에서 이동 할 수 있는 좌표라면
				if vilige[curY][curX]==GROUND and vilige[nY][nX]==GROUND: # 체력 소모 없이 이동하는 경우,
					if not visited[nY][nX][curHP]: # 방문 하지 않았을 경우만(이미 방문 했다는 건 현재 요소 보다 빠른 경로가 존재한다는 의미이기 때문)
						visited[nY][nX][curHP]=True
						q.append((nY,nX,curHP,curTime+1))
				else: # 체력 소모와 함께 이동하는 경우
					if curHP>0 and not visited[nY][nX][curHP-1]: # 위와 동문
						visited[nY][nX][curHP-1]=True
						q.append((nY,nX,curHP-1,curTime+1))
	
	return False

N,M,T=map(int,input().split())
vilige=[list(map(int,input().split())) for _ in range(N)]

start=0
end=N*M-1

while start<=end: # 컨디션이 클 수록 조건(T초 이하로 도달 가능)을 만족 시키는 경향이 있다. 즉 특정 컨디션 이후로부터는 쭉 만족 시킨다.(이분탐색 활용 가능)
	
	mid=(start+end)//2
	tmp=solution(vilige,mid,T)
	if tmp==1:
		end=mid-1
	else:
		start=mid+1

if 0<=start<N*M : print(start)
else : print(-1)