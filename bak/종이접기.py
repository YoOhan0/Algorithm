import sys
def solution(target):
    
    if len(target)==1: return True

    mid=len(target)//2
    flag=True
    for i in range(mid):
        if target[i]==target[len(target)-i-1]:
            flag=False
    
    if flag==True:
        m=solution(target[0:mid])
        n=solution(target[mid+1:len(target)])
        if m and n: return True
        else : return False

    else:
        return False

T=int(input())
for _ in range(T):
    answer=solution(input())
    if answer==True:
        print("YES")
    else:
        print("NO")