import sys
input=sys.stdin.readline

N=int(input())
M=int(input())

ss=[i for i in range(N+1)]

def bindSS(t1,t2):
    global ss
    
    if checkSS(t1,t2): return

    while ss[t2]!=t2:
        t2=ss[t2]
    ss[t2]=t1

def checkSS(t1,t2):
    global ss
    while ss[t1]!=t1:
        t1=ss[t1]
    while ss[t2]!=t2:
        t2=ss[t2]
    return t1==t2

for i in range(N):
    tmp=list(map(int,input().split()))
    for j in range(N):
        
        if tmp[j]: 
            bindSS(i+1,j+1)

plan=list(map(int,input().split()))

flag=True
for i in range(M-1):
    if not checkSS(plan[i],plan[i+1]): flag=False

if flag: print("YES")
else: print("NO")
        


