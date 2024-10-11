import sys
input=sys.stdin.readline
MAX=1987654321

def solution(curIdx,start,link,startN,linkN): # curIdx 선택(고려)하는 함수
    global answer

    if startN > N//2 or linkN > N//2: return
    elif startN==N//2 and linkN==N//2:
        answer=min(answer,calScore(start,link))
        return

    solution(curIdx+1,start+[curIdx],link,startN+1,linkN)
    solution(curIdx+1,start,link+[curIdx],startN,linkN+1)

def calScore(start,link):

    startSum=0
    linkSum=0
    for i in range(N//2):
        for j in range(i+1,N//2):
            startSum+= ability[start[i]][start[j]]+ability[start[j]][start[i]]
            linkSum+= ability[link[i]][link[j]]+ability[link[j]][link[i]]

    return abs(startSum-linkSum)

N=int(input())  

ability=[]
for _ in range(N):
    ability.append(list(map(int,input().split())))

answer=MAX

solution(0,[],[],0,0)
print(answer)