# 백트래킹 및 비트 마스킹 이용
import sys
sys.setrecursionlimit(10**6)

def solution(cur,cnt):
    global N,check,ansCnt,ansArr
    if cur==0 and cnt>ansCnt: # 백트래킹으로 진행하다가, 비트 마스킹이 0이 됬는데 cnt가 지금까지 구한 최대 cnt 보다 크면 정답에 반영
        ansCnt=cnt
        ansArr=list(curArr)
        return
        
    for i in range(N):
        if (cur & (1<<i)) > 0: # 비트 마스킹 상으로, 현재 for문으로 보는 자리에 해당하는 연극단원이 있을 때
            if cur ^ (1<<i) == 0 or not check[cur ^ (1<<i)]:
                check[cur ^ (1<<i)]=True                
                curArr.append(i+1)
                solution(cur^(1<<i),cnt+1)
                curArr.pop()

        if (cur & (1<<i)) ==0 and not check[cur | (1<<i)]: # 비트 마스킹 상으로, 현재 for문으로 보는 자리에 해당하는 연극단원이 없을을 때
            check[cur | (1<<i)]=True
            curArr.append(i+1)
            solution(cur|(1<<i),cnt+1)
            curArr.pop()

check=[False for _ in range(2**17)]
ansCnt=0
ansArr=[]
curArr=[]

N=int(input())

solution(0,0)

print(ansCnt-1)
for item in ansArr:
    print(item)