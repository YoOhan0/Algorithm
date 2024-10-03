import sys

input=sys.stdin.readline

def solution(N):
    costums={}

    for _ in range(N):
        costum, costumType= input().split()
        if costums.get(costumType):
            costums[costumType]+=1
        else:
            costums[costumType]=1

    answer=1
    for i in costums.values():
        answer*=(i+1)

    return answer-1

testCnt=int(input())

for _ in range(testCnt):
    N=int(input())
    print(solution(N))
