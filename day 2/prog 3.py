# write a python program to print the number which are not divisible by 6,7 and 8 in a given range?
n,m=int(input()),int(input())
for i in range(n,m+1):
    if i%6!=0 and i%7!=0 and i%8!=0:
        print(i)
