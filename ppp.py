#wap yo remove duplicate from the list
a=[10,20,10,30]
b=[]
for i in range(len(a)):
    if a[i] not in b:
        b.append(a[i])
print(b)