import sys
input=sys.stdin.readline

N=int(input())
nums=list(map(int,input().split()))

nums.sort()
goodNum=0
for i in range(N):
    start=0
    end=N-1
    while start<=end:

        if nums[start]+nums[end]==nums[i]:
            if start!=i and end != i: break
            elif start==i : start+=1
            elif end==i : end-=1

        elif nums[start]+nums[end]>nums[i]:
            end-=1
        elif nums[start]+nums[end]<nums[i]:
            start+=1
    if start<end: goodNum+=1

print(goodNum)