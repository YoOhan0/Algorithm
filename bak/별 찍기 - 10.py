import sys
input=sys.stdin.readline
print=sys.stdout.write
def solution(baseY,baseX,size):
    nSize=size//3
    if nSize==1:
        save[baseY]+="***"
        save[baseY+1]+="* *"
        save[baseY+2]+="***"
        return
                
    for i in range(3):
        for j in range(3):
            if i==1 and j==1:
                for k in range(nSize):
                    save[baseY+nSize*i+k]+=" "*nSize
            else:
                solution(baseY+nSize*i,baseX+nSize*j,nSize)
    return

N=int(input())
save=[""]*2187 # 3^7
solution(0,0,N)
print('\n'.join(save[:N]))