#write a python program to reverse of a number using while loop?
'''n=int(input())
rev=0
while n > 0:
    digit=n%10
    rev=rev*10+digit
    n//=10
print(rev)'''
n=int(input())
rev=0
for i in range(n):
 if n > 0:
    digit=n%10
    rev=rev*10+digit
    n//=10
 else:
    break
print(rev)
