#write a python program to print factorial of a number.
def fact(n):
    if n < 1:
        return 1
    else:
        return n*fact(n-1)
n=int(input())
print(fact(n))
