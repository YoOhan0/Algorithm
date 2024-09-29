import sys

def backTrack(cur,sum):
    global N,advices 
    
    max=sum # 재귀에 마지막에 해당하는 경우는 선택된 날짜들의 금액의 합을 의미하고, 나머지 경우에는 아래에서 위로 올라오면서 최대값을 고려하는 역할.
    for i in range(cur,N):
        if i+advices[i][0]<=N:
            tmp=backTrack(i+advices[i][0],sum+advices[i][1])
            if max<tmp: max=tmp

    return max

input= sys.stdin.readline

N= int(input())

advices=[[0]*2 for _ in range(N)]

for i in range(N):
    advices[i][0], advices[i][1]=map(lambda x: int(x),input().split())

print(backTrack(0,0))

