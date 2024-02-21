'''x,n=map(int,input().split())
ns=n*x
if ns%4==0:
    np=ns//4
else:
    np=(ns//4)+1
print(np)'''
import math
x,n=map(int,input().split())
ns=n*x
np=math.ceil(c/4)
print(np)

