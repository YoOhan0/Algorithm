import sys
input=sys.stdin.readline
MAX=2000000000

def solution(waters):
    global answerSum,answer
    start=0
    end=len(waters)-1

    while start<end:
        
        target=waters[start]+waters[end]
        
        if answerSum>=abs(target):
            answerSum=abs(target)
            answer=(waters[start],waters[end])
        
        if target==0:
            break
        elif target>0:
            end-=1
        elif target<0:
            start+=1

    return

N=int(input())

waters=list(map(int,input().split()))
waters.sort()

answerSum=MAX
answer=(0,0)

solution(waters)

print(f"{min(answer)} {max(answer)}")