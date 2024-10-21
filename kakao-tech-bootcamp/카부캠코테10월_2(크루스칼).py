import heapq

def together(target1,target2): 
	
    if check(target1)==check(target2): 
        return
	
    root1=check(target1)
    root2=check(target2)
    if rank[root1]<rank[root2]: # 분리 집합의 뿌리의 길이가 짧은 것을 큰 분리 집합에 붙여야, 이후 분리 집합의 뿌리 길이가 최적화 됨(Rank 최적화)
         ss[root1]=root2
    elif rank[root1]>rank[root2]:
         ss[root2]=root1
    else:
         ss[root1]=root2
         rank[root2]+=1

def check(target): #분리 집합의 find 함수에 경로 압축 최적화 적용
	global ss
	if ss[target]!=target:
		ss[target]=check(ss[target])
	return ss[target]
	
N=int(input())
M=int(input())
already=[tuple(map(int,input().split())) for _ in range(M)]
K=int(input())
possible=[tuple(map(int,input().split())) for _ in range(K)]

ss=[i for i in range(N+1)]
rank=[1 for _ in range(N+1)]

pq=[]
for i in range(M):
    heapq.heappush(pq,(0,already[i][0],already[i][1]))
for i in range(K):
    heapq.heappush(pq,(possible[i][2],possible[i][0],possible[i][1]))

answer=0
while pq:
    cost,target1,target2=heapq.heappop(pq)
    if check(target1)!=check(target2):
        together(target1,target2)
        answer+=cost

flag=False
for i in range(1,N):
    if check(i)!=check(i+1):
        flag=True
        break

if flag: print(-1)
else: print(answer)