import sys
input=sys.stdin.readline

N=int(input())
A=list(map(int,input().split()))
B,C=map(int,input().split())

cnt=0
for i in A:
    i-=B
    if i>0:
        cnt+=i//C
        if i%C>0:cnt+=1

print(N+cnt)