import sys
input=sys.stdin.readline
INF=1987654321

def solution(citys):
    global C,N
    dp=[INF]*1001 # dp[최소 j명의 사람 수 고려]= 했을 때의 최소 비용 값

    for cost,profit in citys:
        for j in range(1001):
            if j<=profit: dp[j]=min(dp[j],cost)
            else: dp[j]=min(dp[j],cost+dp[j-profit])
        # print(dp[:13])
    return dp[C]

C,N=map(int,input().split())

citys=[tuple(map(int,input().split())) for _ in range(N)]

print(solution(citys))