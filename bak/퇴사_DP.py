import sys

input=sys.stdin.readline

N=int(input())

advices=[[0]*2 for _ in range(N)]
dp=[0 for _ in range(N)]

for i in range(N):
    advices[i][0],advices[i][1]= map(lambda x:int(x),input().split())

if advices[0][0]-1<N: dp[advices[0][0]-1]=advices[0][1] # dp[0] 초기화

for i in range(1,N): # dp 의미: i까지의 요소들을 고려 했을 때 만들 수 있는 최대 금액.
   
    if advices[i][0]+i-1<N: # 회사에 없는 날에는 상담을 할 수 없다.
        
        dp[advices[i][0]+i-1]=max(dp[advices[i][0]+i-1],advices[i][1]+dp[i-1]) # max(i-1 까지의 최대 + 현재 상담일 금액, 이전까지의 최대) -> 상담기간의 마지막날을 포함하는 경우를 고려.

    dp[i]=max(dp[i],dp[i-1]) # i 까지의 최대를 구할때, i를 포함하지 않는 경우들도 고려해주어야 된다.

print(dp[N-1])
