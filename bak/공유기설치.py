# <이분탐색>

# 문제에서 목표로 하는 값을 대상으로, 가능한 범위 내에서 문제에서 주어진 조건을
# 여유 있게 만족 하느냐 혹은 부족 하느냐에 따라 이분 탐색 하면서 최적(최대,최소)의 목표를 찾는 방식의 알고리즘

# 장점 : 탐색을 선형(O(n))으로 하지 않고, O(log(n))으로 수행함으로써 시간 복잡도적인 이점이 있다.
# 단점 : 문제마다 적용 할 수 있는지 여부를 설계 잘 해야한다.

import sys

input=sys.stdin.readline

def solution():
    N,C=map(int,input().split())

    homes=[]
    for _ in range(N):
        homes.append(int(input()))

    homes.sort()

    start=1
    end=1000000000
    while start<=end:

        cur=(start+end)//2
        
        cnt=1
        base=0
        for i in range(N):
            if homes[i]-homes[base]>=cur:
                base=i
                cnt+=1
    
        if cnt<C:
            end=cur-1
        else:
            start=cur+1

    print(end)

solution()

