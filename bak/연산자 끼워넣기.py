import sys
input=sys.stdin.readline
MAX=1987654321

def solution(plus,minus,mul,div,A,curIdx,curNum):
    global answerMax,answerMin
    if curIdx==N:
        if answerMax<curNum: answerMax=curNum
        if answerMin>curNum: answerMin=curNum
        return

    if plus>0: solution(plus-1,minus,mul,div,A,curIdx+1,curNum+A[curIdx])
    if minus>0: solution(plus,minus-1,mul,div,A,curIdx+1,curNum-A[curIdx])
    if mul>0: solution(plus,minus,mul-1,div,A,curIdx+1,curNum*A[curIdx])
    if div>0: 
        if curNum<0: tmp=-((-curNum)//A[curIdx])
        else: tmp=curNum//A[curIdx]
        solution(plus,minus,mul,div-1,A,curIdx+1,tmp)

N=int(input())
A=list(map(int,input().split()))

plus,minus,mul,div=map(int,input().split())
answerMax=-MAX
answerMin=MAX

solution(plus,minus,mul,div,A,1,A[0])
print(answerMax)
print(answerMin)