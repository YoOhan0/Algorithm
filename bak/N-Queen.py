# 현재 위치에서 x,y 좌표를 이용하여 자기가 속한 고유한 대각선(left,right)을 알 수 있음!! 
# leftCross[27]: 왼쪽 대각선
    #     0 0 0 0 (3) 
    #     0 0 0 0 (2)
    #     0 0 0 0 (1)
    #     0 0 0 0 (0)
    #   (-3)(-2)(-1)
    # -> leftCross[col-row+N-1] : 현재 지점의 왼쪽 대각선 가능 여부(가능한 배열 최대값: 27(because N 최대 14))

    # rightCross[27]: 오른쪽 대각선
    #    (0) 0 0 0 0
    #    (1) 0 0 0 0
    #    (2) 0 0 0 0
    #    (3) 0 0 0 0
    #        (4)(5)(6)
   
    #    -> rightCross[row+col] : 현재 지점의 오른쪽 대각선 가능 여부(가능한 배열 최대값: 27(because N 최대 14))
import sys

input=sys.stdin.readline

def solution(curRow,curCol,chassCnt):
   
   if chassCnt==N: return 1

   vertical[curCol]+=1
   leftCross[curCol-curRow+N-1]+=1
   rightCross[curRow+curCol]+=1
   
   answer=0
   nextRow=curRow+1
   for nextCol in range(N):
        if not vertical[nextCol] and not leftCross[nextCol-nextRow+N-1] and not rightCross[nextRow+nextCol]:
            answer+=solution(nextRow,nextCol,chassCnt+1)

   vertical[curCol]+=-1
   leftCross[curCol-curRow+N-1]+=-1
   rightCross[curRow+curCol]+=-1
   
   return answer

N=int(input())

leftCross=[0]*(2*(N-1)+1)
rightCross=[0]*(2*(N-1)+1)
vertical=[0]*N

answer=0
for i in range(N):
    answer+=solution(0,i,1)

print(answer)