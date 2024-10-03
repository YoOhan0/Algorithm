import sys

input=sys.stdin.readline

def solution():
    N,L=map(int,input().split())

    holes=list(map(int,input().split()))

    holes.sort()

    maxTape=holes[0]+L
    tapeCnt=1
    for i in range(N): # 정렬 시키고, 앞에서 부터 최대한 한 테이프에 많은 구멍을 막는 로직.
        if holes[i]<maxTape:
            continue
        else:
            maxTape=holes[i]+L
            tapeCnt+=1

    print(tapeCnt)

solution()