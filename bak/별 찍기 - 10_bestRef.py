import sys
input=sys.stdin.readline

def solution(size):
    if size==1:
        return "*"
    nSize=size//3

    parts=solution(nSize)
    answer=[]
    for part in parts:
        answer.append(3*part)
    for part in parts:
        answer.append(part+" "*nSize+part)
    for part in parts:
        answer.append(3*part)
    return answer

N=int(input())
for line in solution(N):
    print(line)