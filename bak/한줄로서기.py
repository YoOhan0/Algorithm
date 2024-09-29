N=int(input())

persons=list(map(lambda x:int(x),input().split(" ")))

answer=[N]

# 키가 제일 높은 사람부터 반복문을 돌며,줄을 세운다.(반복문을 역순으로 하면서, 하나씩 줄에 배치 시켜야 위치를 정확히 배치 시킬 수 있음)
for i in range(N-2,-1,-1):
    answer.insert(persons[i],i+1)
    
for i in answer:
    print(i,end=" ")


