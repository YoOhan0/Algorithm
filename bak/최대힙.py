import sys
from queue import PriorityQueue
input=sys.stdin.readline

N=int(input())

pq=PriorityQueue()

for _ in range(N):
    x=int(input())
    if x==0:
        if pq.empty():
            print(0)
        else:
            print(pq.get())
    else:
        pq.put(x)



