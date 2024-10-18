import sys
input=sys.stdin.readline
INF=1987654321
def solution(info):
    global C,N
    dp=[[INF]*(C+1)]*(N+1)
    for i in range(N+1):dp[i][0]=0
    
    for i in range(1,N+1):
        curCost,curProfit=info[i]
        for totalProfit in range(1,C+1):
            cnt=totalProfit//curProfit
            remain=totalProfit%curProfit
            dp[i][totalProfit]=min(dp[i-1][totalProfit],curCost*(cnt+1))
            for k in range(1,cnt+1):
                dp[i][totalProfit]=min(dp[i][totalProfit],dp[i-1][remain+(cnt-k)*curProfit]+curCost*k)

    return dp[N][C]
           
C,N=map(int,input().split())
info=[[]]
for _ in range(N): info.append(tuple(map(int,input().split())))
print(solution(info))