import sys
input=sys.stdin.readline

MAXHP=100
N=int(input())

L=list(map(int,input().split()))
J=list(map(int,input().split()))

dp=[[0]* MAXHP for _ in range(N)]

for i in range(N): # 각각의 요소들 하나씩 누적해서 고려해 나간다.
    for j in range(MAXHP):
        
        if j<L[i]: dp[i][j]=dp[i-1][j]
        elif i==0: dp[i][j]=J[i] # i 반복문 첫 번째 루프 고려.
        elif j>=L[i]: dp[i][j]=max(dp[i-1][j] ,dp[i-1][j-L[i]]+J[i])

print(max(dp[N-1]))
