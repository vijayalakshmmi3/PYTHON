#write a python program to remove the duplicates in a list.
l=list(map(int,input().split()))
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
print(l1)
        
