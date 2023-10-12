from random import *
b1,b2,b3=0,0,0
n = randint(1,3)


if n==1:b1=1 ;emptybox1=b2;emptybox2=b3
elif n==2:b2=1;emptybox1=b1;emptybox2=b3
else:b3=1;emptybox1=b2;emptybox2=b1
boxes=[b1,b2,b3]

pick=int(input())
