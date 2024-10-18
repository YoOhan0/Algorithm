import sys
input=sys.stdin.readline

def solution(baseY,baseX,size,cnt):
    if size==1:
        return cnt
    global r,c
    nSize=size//2
    part=(size*size)//4

    if baseY<=r<baseY+nSize and baseX<=c<baseX+nSize:
        return solution(baseY,baseX,nSize,cnt)
    elif baseY<=r<baseY+nSize and baseX+nSize<=c<baseX+2*nSize:
        return solution(baseY,baseX+nSize,nSize,cnt+part)
    elif baseY+nSize<=r<baseY+2*nSize and baseX<=c<baseX+nSize:
        return solution(baseY+nSize,baseX,nSize,cnt+2*part)
    elif baseY+nSize<=r<baseY+2*nSize and baseX+nSize<=c<baseX+2*nSize:
        return solution(baseY+nSize,baseX+nSize,nSize,cnt+3*part)
    
N,r,c=map(int,input().split())

print(solution(0,0,2**N,0))