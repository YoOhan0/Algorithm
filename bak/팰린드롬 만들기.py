import sys
input=sys.stdin.readline
print=sys.stdout.write

def solution():
    answer=[]
    alpha=[0]*26
    q=[]
    odd=[]
    for i in range(len(name)):
        alpha[ord(name[i])-ord('A')]+=1

    for i in range(26):
        if alpha[i]:
            answer.append(chr(ord('A')+i)*(alpha[i]//2))
            q.append(chr(ord('A')+i)*(alpha[i]//2))
            if alpha[i]%2!=0:
                odd.append(chr(ord('A')+i))
            
    if (len(name)%2 and len(odd)>1) or (not len(name)%2 and len(odd)):
        print("I'm Sorry Hansoo")
        return
    else: q.extend(odd)
    
    for i in answer: print(i)
    while len(q):
        print(q.pop())

name=input().strip()
solution()