import sys

def func():
    st1=[]
    st2=[]

    inputStr=input().strip()
    
    for j in inputStr:

        if j=='<':
            if st1:
                st2.append(st1.pop())
        elif j=='>':
            if st2:
                st1.append(st2.pop())
        elif j=='-':
            if st1:
                st1.pop()
        else:
            st1.append(j)
    
    print(''.join(st1+st2[::-1]))


input=sys.stdin.readline

N=int(input().strip())

for i in range(N):
    func()

