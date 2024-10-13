import sys
input=sys.stdin.readline

LEFT=0
UP=1
RIGHT=2
DOWN=3

def solution(board,cnt):
    if cnt==5: return 0
    maxNum=0
    for i in range(4):
        newBoard,tmpNum=makeBoard(board,i)
        if maxNum<tmpNum: maxNum=tmpNum #현재 단계에서 만들 수 있는 최대 값을 고려.
        maxNum=max(maxNum,solution(newBoard,cnt+1)) # 이후 진행 된 것들에서의 최대값들도 고려.

    return maxNum
    
def makeBoard(board,dir):
    steps=[()]
    newBoard=[[0]*N for _ in range(N)]
    maxNum=0
    if dir==LEFT or dir==RIGHT:
        for i in range(N):
            bucket=[]
            prev=-1
            for j in range(N):
                if dir==LEFT and not board[i][j]: continue
                if dir==RIGHT and not board[i][N-1-j]: continue

                if prev==-1:
                    if dir==LEFT: prev=board[i][j]
                    else: prev=board[i][N-1-j]
                else:

                    if dir==LEFT and prev==board[i][j]:
                        bucket.append(2*board[i][j])
                        prev=-1
                    elif dir==RIGHT and prev==board[i][N-1-j]:
                        bucket.append(2*board[i][N-1-j])
                        prev=-1
                    else:
                        bucket.append(prev)
                        if dir==LEFT:prev=board[i][j]
                        else: prev=board[i][N-1-j]
            if prev!=-1: bucket.append(prev)
            for idx,item in enumerate(bucket):
                if item>maxNum: maxNum=item
                if dir==LEFT: newBoard[i][idx]=item
                else: newBoard[i][N-1-idx]=item

    if dir==UP or dir==DOWN:
        for i in range(N):
            bucket=[]
            prev=-1
            for j in range(N):
                if dir==UP and not board[j][i]: continue
                if dir==DOWN and not board[N-1-j][i]: continue

                if prev==-1:
                    if dir==UP:prev=board[j][i]
                    else: prev=board[N-1-j][i]
                else:
                    if dir==UP and prev==board[j][i]:
                        bucket.append(2*board[j][i])
                        prev=-1
                    elif dir==DOWN and prev==board[N-1-j][i]:
                        bucket.append(2*board[N-1-j][i])
                        prev=-1
                    else:
                        bucket.append(prev)
                        if dir==UP:prev=board[j][i]
                        else: prev=board[N-1-j][i]
            if prev!=-1: bucket.append(prev)
            for idx,item in enumerate(bucket):
                if item>maxNum: maxNum=item
                if dir==UP:newBoard[idx][i]=item
                else: newBoard[N-1-idx][i]=item
    return (newBoard,maxNum)

N=int(input())
board=[]

for _ in range(N):
    board.append(list(map(int,input().split())))

print(solution(board,0))
