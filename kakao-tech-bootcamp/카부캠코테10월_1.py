N=int(input())
H=list(map(int,input().split()))

time=0
for i in range(N):
	targetHP=H[i]
	answer=targetHP//10
	remain=targetHP%10
	while remain>0:
		remain-=time%4+1
		time+=1
	
print(time)

# i%4+1
# i=1 1+0 =1
# i=2 1+1 =2
# i=3 1+2 =3
# i=4 1+3 =4
# i=5 1+ 0