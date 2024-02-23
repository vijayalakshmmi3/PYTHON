#write a python program to print average of max and min element in a matrix using tuple.
r,c=int(input()),int(input())
l,sum=[],0
for i in range (r):
    l.append(tuple(map(int,input().split())))
min,max=1000,0
for i in l:
    for j in i:
        sum+=j
print(sum/(r*c))
