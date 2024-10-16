import sys
input=sys.stdin.readline

def solution(horses,commands,curIdx,total):
    global game,score,N,answer
    if curIdx==N:
        if answer<total:
            answer=total
        return

    for idx,horse in enumerate(horses):
        if horse==22: continue
        if len(game[horse])==2: tmpHorse=game[horse][1]
        else : tmpHorse=game[horse][0]
        tmpCnt=commands[curIdx]-1
        while tmpCnt>0:
            tmpHorse=game[tmpHorse][0]
            tmpCnt-=1
        if tmpHorse==22 or tmpHorse not in horses:
            next=[horses[0],horses[1],horses[2],horses[3]]
            next[idx]=tmpHorse
            solution(next,commands,curIdx+1,total+score[tmpHorse])

game={1:[2],2:[3],3:[4],4:[5],5:[6],6:[7,31],7:[8],8:[9],9:[10],10:[11],11:[12,41],12:[13],13:[14],14:[15],15:[16],16:[17,51],17:[18],18:[19],19:[20],20:[21],21:[22],22:[22],
      31:[32],32:[33],33:[100],
      41:[42],42:[100],
      51:[52],52:[53],53:[100],
      100:[61],61:[62],62:[21]}
score={1:0,2:2,3:4,4:6,5:8,6:10,7:12,8:14,9:16,10:18,11:20,12:22,13:24,14:26,15:28,16:30,17:32,18:34,19:36,20:38,21:40,22:0,
       31:13,32:16,33:19,
       41:22,42:24,
       51:28,52:27,53:26,
       100:25,61:30,62:35}

commands=list(map(int,input().split()))
N=len(commands)
answer=0

solution([1,1,1,1],commands,0,0)
print(answer)