d=[1,2,3]
for i in range(len(d)):
    for j in range(len(d)):
        for k in range(len(d)):
            if(i!=j&j!=k&k!=i):
                print(d[i],d[j],d[k])