# wap to find how many times  a given element occur in a tuple
a=input()
l1=a.split(",")
t1=tuple(l1)
c=0
b=int(input())
for i in t1:
    if b==int(i):
        c+=1
if c==0:
    print("not in tuple")
else:
    print(c)
