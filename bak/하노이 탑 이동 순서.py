import sys
input= sys.stdin.readline
print=sys.stdout.write

def hanoi(main,second,goal,lowLayer):

    if second==goal or lowLayer==1:
        answer.append((main,goal))
        return 1
    sum=0
    sum+=hanoi(main,goal,second,lowLayer-1)
    sum+=hanoi(main,goal,goal,lowLayer)
    sum+=hanoi(second,main,goal,lowLayer-1)
    return sum


N=int(input())
answer=[]
print(str(hanoi(1,2,3,N))+"\n")
for i in answer:
    print(f"{i[0]} {i[1]}\n")